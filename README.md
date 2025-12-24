# 🎥 YouTube Search Application

<div align="center">

![Python](https://img.shields.io/badge/Python-60.8%25-blue.svg)
![HTML](https://img.shields.io/badge/HTML-36.5%25-orange.svg)
![CSS](https://img.shields.io/badge/CSS-2.7%25-purple.svg)
![Django](https://img.shields.io/badge/Django-Framework-green.svg)
![YouTube API](https://img.shields.io/badge/YouTube-API%20v3-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**A powerful web application that leverages YouTube Data API v3 to search, display, and play videos directly in the browser**

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [API Setup](#api-setup) • [Usage](#usage)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [API Integration](#api-integration)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [API Endpoints](#api-endpoints)
- [Future Enhancements](#future-enhancements)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🎯 Overview

The **YouTube Search Application** is a full-stack web application built with Django that provides a seamless interface to search and watch YouTube videos. By integrating YouTube Data API v3, users can search for videos, view detailed information, and play content directly within the application without leaving the page.

### Key Highlights
- 🔍 **Real-Time Search**: Instant video search using YouTube API
- ▶️ **Embedded Player**: Watch videos directly in the application
- 📊 **Rich Metadata**: Display views, likes, duration, and channel info
- 🎨 **Clean UI**: Modern, responsive design for optimal user experience
- ⚡ **Fast Performance**: Optimized API calls with caching
- 🔐 **Secure**: API key management with environment variables

This project demonstrates:
- **API Integration**: RESTful API consumption and data parsing
- **Full-Stack Development**: Django backend with dynamic frontend
- **Data Handling**: JSON parsing and data transformation
- **User Interface Design**: Responsive and intuitive UI/UX

---

## ✨ Features

### 🔍 Search Functionality
- **Smart Search**: Search YouTube's entire video library
- **Real-Time Results**: Instant search results as you type
- **Pagination**: Browse through multiple pages of results
- **Sort Options**: Sort by relevance, date, views, rating
- **Filters**: Filter by video duration, upload date, quality

### ▶️ Video Player
- **Embedded Player**: Watch videos without leaving the site
- **Responsive Player**: Adapts to different screen sizes
- **Playback Controls**: Full YouTube player controls
- **Autoplay Option**: Queue and autoplay videos
- **Quality Selection**: Choose video quality

### 📊 Video Information
- **Thumbnails**: High-quality video thumbnails
- **Metadata Display**: 
  - Video title and description
  - Channel name and subscriber count
  - View count and like count
  - Upload date and duration
  - Tags and categories

### 🎨 User Interface
- **Responsive Design**: Mobile-friendly layout
- **Grid View**: Organized video grid display
- **Dark/Light Theme**: Theme toggle support
- **Search History**: Recent searches saved
- **Loading States**: Smooth loading animations

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 4.0+
- **Language**: Python 3.8+ (60.8%)
- **Database**: SQLite3
- **API Client**: google-api-python-client
- **HTTP Library**: requests

### Frontend
- **Templates**: Django Templates
- **HTML5**: Semantic markup (36.5%)
- **CSS3**: Custom styling (2.7%)
- **JavaScript**: Dynamic interactions
- **Responsive**: Mobile-first design

### External Services
- **YouTube Data API v3**: Video search and metadata
- **YouTube Player API**: Embedded video player

---

## 🔌 API Integration

### YouTube Data API v3

The application uses the following API endpoints:

#### 1. Search Videos
```python
youtube.search().list(
    part='snippet',
    q=search_query,
    maxResults=20,
    type='video',
    order='relevance'
)
```

#### 2. Get Video Details
```python
youtube.videos().list(
    part='snippet,statistics,contentDetails',
    id=video_id
)
```

#### 3. Get Channel Information
```python
youtube.channels().list(
    part='snippet,statistics',
    id=channel_id
)
```

### API Response Handling
```python
def parse_video_data(response):
    """Parse YouTube API response"""
    videos = []
    for item in response['items']:
        video = {
            'id': item['id']['videoId'],
            'title': item['snippet']['title'],
            'thumbnail': item['snippet']['thumbnails']['high']['url'],
            'channel': item['snippet']['channelTitle'],
            'description': item['snippet']['description'],
            'published_at': item['snippet']['publishedAt']
        }
        videos.append(video)
    return videos
```

---

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- YouTube Data API key ([Get one here](https://console.cloud.google.com/))
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ashwinder0186/youtube.git
cd youtube
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Get YouTube API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable YouTube Data API v3
4. Create credentials (API key)
5. Copy the API key

### Step 5: Configure Environment Variables
Create a `.env` file in the root directory:
```env
YOUTUBE_API_KEY=your_youtube_api_key_here
SECRET_KEY=your_django_secret_key
DEBUG=True
```

Or update `settings.py`:
```python
YOUTUBE_API_KEY = 'your_youtube_api_key_here'
```

### Step 6: Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## ⚙️ Configuration

### API Key Setup

#### Method 1: Environment Variables (Recommended)
```python
# settings.py
import os
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
```

#### Method 2: Direct Configuration
```python
# settings.py
YOUTUBE_API_KEY = 'AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

### API Quota Management
YouTube API has daily quota limits:
- **Free Tier**: 10,000 units/day
- **Search query**: 100 units
- **Video details**: 1 unit

To optimize quota usage:
```python
# Cache search results
from django.core.cache import cache

def search_videos(query):
    cache_key = f'search_{query}'
    results = cache.get(cache_key)
    if not results:
        results = youtube_api_call(query)
        cache.set(cache_key, results, 3600)  # Cache for 1 hour
    return results
```

---

## 🚀 Usage

### Basic Search

1. **Home Page**
   - Enter search query in the search box
   - Click "Search" or press Enter

2. **View Results**
   - Browse through video thumbnails
   - See video titles, channels, views, and upload dates

3. **Play Video**
   - Click on any video thumbnail
   - Video plays in embedded player
   - View full video details below player

### Advanced Search

```python
# Add filters to search
def advanced_search(query, duration='any', order='relevance'):
    youtube.search().list(
        q=query,
        type='video',
        part='snippet',
        maxResults=20,
        videoDuration=duration,  # short, medium, long, any
        order=order  # relevance, date, rating, viewCount
    )
```

### Search Examples
- Simple: `"Python tutorial"`
- Channel: `"channel:TechWithTim"`
- Filters: `"Python tutorial duration:long"`
- Date: `"Python tutorial after:2023-01-01"`

---

## 📁 Project Structure

```
youtube/
│
├── manage.py                  # Django management script
├── db.sqlite3                 # SQLite database
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
│
├── youtube_search/            # Main Django app
│   ├── __init__.py
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI config
│   └── asgi.py               # ASGI config
│
├── search/                    # Search functionality app
│   ├── models.py             # Database models
│   ├── views.py              # View controllers
│   ├── urls.py               # App URLs
│   ├── forms.py              # Search forms
│   └── youtube_api.py        # API integration
│
├── templates/                 # HTML templates
│   ├── base.html             # Base template
│   ├── search.html           # Search page
│   ├── results.html          # Results display
│   └── video.html            # Video player page
│
├── static/                    # Static files
│   ├── css/
│   │   └── styles.css        # Custom styles
│   ├── js/
│   │   └── scripts.js        # JavaScript
│   └── images/
│       ├── back.jpg          # Background image
│       └── back copy.jpg     # Alt background
│
└── README.md                  # This file
```

---

## 📸 Screenshots

### Home Page - Search Interface
*Clean, intuitive search interface with YouTube branding*

### Search Results Grid
*Responsive grid layout displaying video thumbnails and metadata*

### Video Player Page
*Embedded YouTube player with full video information*

### Mobile View
*Fully responsive design for mobile devices*

---

## 🔗 API Endpoints

### Application Routes

```python
# urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('video/<str:video_id>/', views.video_detail, name='video_detail'),
    path('channel/<str:channel_id>/', views.channel_info, name='channel_info'),
]
```

### View Functions

```python
# views.py

def search(request):
    """Handle video search"""
    query = request.GET.get('q', '')
    videos = youtube_api.search_videos(query)
    return render(request, 'results.html', {'videos': videos})

def video_detail(request, video_id):
    """Display video player and details"""
    video = youtube_api.get_video_details(video_id)
    return render(request, 'video.html', {'video': video})
```

---

## 🔮 Future Enhancements

### Features
- [ ] **User Authentication**: Save favorite videos and playlists
- [ ] **Watch History**: Track viewed videos
- [ ] **Recommendations**: ML-based video suggestions
- [ ] **Playlist Creation**: Create and manage custom playlists
- [ ] **Comments Display**: Show video comments from YouTube
- [ ] **Download Option**: Download videos (respecting YouTube ToS)

### Technical Improvements
- [ ] **Redis Caching**: Implement Redis for better caching
- [ ] **Elasticsearch**: Add full-text search capabilities
- [ ] **GraphQL API**: Create GraphQL endpoints
- [ ] **WebSocket**: Real-time updates and notifications
- [ ] **PWA**: Convert to Progressive Web App
- [ ] **Docker**: Containerize application

### UI/UX Enhancements
- [ ] **Dark Mode**: Complete dark theme implementation
- [ ] **Keyboard Shortcuts**: Add hotkeys for navigation
- [ ] **Infinite Scroll**: Replace pagination with infinite scroll
- [ ] **Advanced Filters**: More search filter options
- [ ] **Video Preview**: Hover to preview video clips
- [ ] **Multi-Language**: Support for multiple languages

---

## 🐛 Troubleshooting

### Common Issues

#### API Key Errors
```bash
Error: The request cannot be completed because you have exceeded your quota.
```
**Solution**: Check your API quota usage in Google Cloud Console

#### Video Playback Issues
```bash
Error: Video unavailable or playback restricted
```
**Solution**: Some videos have embedding restrictions. Check video settings.

#### Import Errors
```bash
ModuleNotFoundError: No module named 'googleapiclient'
```
**Solution**: 
```bash
pip install google-api-python-client
```

### Debug Mode

Enable detailed error messages:
```python
# settings.py
DEBUG = True
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

---

## 📊 Performance Optimization

### Caching Strategy
```python
# Cache API responses
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Cache for 15 minutes
def search(request):
    # View logic
    pass
```

### Database Indexing
```python
# models.py
class SearchHistory(models.Model):
    query = models.CharField(max_length=200, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
```

### Lazy Loading
```javascript
// Lazy load video thumbnails
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                imageObserver.unobserve(img);
            }
        });
    });
    images.forEach(img => imageObserver.observe(img));
});
```

---

## 🔐 Security Considerations

### API Key Protection
- Never commit API keys to version control
- Use environment variables
- Implement rate limiting
- Monitor API usage

### Input Validation
```python
from django.core.validators import validate_slug

def search(request):
    query = request.GET.get('q', '')
    # Sanitize input
    query = query.strip()[:200]  # Limit length
    # Validate query
    if not query or len(query) < 3:
        return render(request, 'error.html')
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Ensure API quota efficiency

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Ashwinder Singh**
- **GitHub**: [@Ashwinder0186](https://github.com/Ashwinder0186)
- **LinkedIn**: [singh-ashwinder](https://linkedin.com/in/singh-ashwinder)
- **Email**: singhashwinder0186@gmail.com
- **Education**: MS in Computer Science, University of Texas at Arlington (GPA: 4.0/4.0)

### Background
Full-stack developer with expertise in Python, Django, and API integration. Experience in building scalable web applications with external API services. Previously worked at Tata Consultancy Services developing automation and analytics tools for financial systems.

**Core Competencies:**
- RESTful API Integration
- Full-Stack Web Development
- Python & Django Framework
- Database Design & Optimization

---

## 🙏 Acknowledgments

- [YouTube Data API v3](https://developers.google.com/youtube/v3) for video data
- [Django Framework](https://www.djangoproject.com/) for robust backend
- [Google API Python Client](https://github.com/googleapis/google-api-python-client) for API integration
- YouTube for providing extensive video platform API

---

## 📚 Resources

### Documentation
- [YouTube API Documentation](https://developers.google.com/youtube/v3/docs)
- [Django Documentation](https://docs.djangoproject.com/)
- [API Best Practices](https://developers.google.com/youtube/v3/guides/best_practices)

### Tutorials
- [YouTube API Quickstart](https://developers.google.com/youtube/v3/quickstart/python)
- [Django REST Framework](https://www.django-rest-framework.org/)

---

## 📞 Support

For issues, questions, or suggestions:
- **Email**: singhashwinder0186@gmail.com
- **Issues**: [Create an issue](https://github.com/Ashwinder0186/youtube/issues)
- **Discussions**: GitHub Discussions tab

---

<div align="center">

**⭐ If you found this project helpful, please consider giving it a star!**

**🎥 Search and Play YouTube Videos Seamlessly**

Made with ❤️ using Django & YouTube API

</div>
