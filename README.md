# Ai-Video-Compression
Original Video
      ↓
Video Compression
      ↓
Compressed / Low-Quality Video
      ↓
AI Deep Learning Filter
      ↓
Enhanced Video
      ↓
Web Dashboard

# Project Architecture
                 ┌──────────────────┐
                 │   User Uploads   │
                 │      Video       │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Extract Video    │
                 │     Frames       │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Simulate H.265/  │
                 │ Compression      │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Compression      │
                 │ Artifacts        │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ AI/DL Filtering  │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Quality Analysis │
                 │ PSNR / SSIM      │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Enhanced Video   │
                 └──────────────────┘

AI_Video_Enhancement/
│
├── app.py
├── video_processor.py
├── requirements.txt
│
├── uploads/
│
├── outputs/
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

                 VIDEO
               ↓
        Frame Extraction
               ↓
       H.265/H.266 Compression
               ↓
       ┌─────────────────┐
       │ CNN / DnCNN /   │
       │ Lightweight AI  │
       │ Filter          │
       └────────┬────────┘
                ↓
        Enhanced Frames
                ↓
        PSNR + SSIM + FPS
                ↓
        Enhanced Video
                ↓
          Web Dashboard

                    To develop a lightweight AI-based video enhancement system that removes compression artifacts while maintaining good video quality, low processing time, and low computational requirements for consumer devices.








                 
