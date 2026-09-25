# Job Searcher

Job Searcher is a personal job aggregation and filtering service designed to collect vacancies directly from company career pages and ATS platforms.

The goal is to reduce irrelevant job recommendations by normalizing job data and matching vacancies against configurable criteria such as role, seniority, location, and skills.

## Features

- Collect jobs directly from ATS platforms (Lever, Greenhouse, Ashby etc.)
- Normalize job data into a common format
- Parse job titles, locations, and skills
- Filter vacancies using configurable matching rules
- Detect newly published vacancies
- Send relevant jobs to Telegram
- Optional AI-assisted vacancy analysis

## How It Works

The application follows a simple processing pipeline:

ATS / Career Page  
→ Raw Job Data  
→ Normalization  
→ Parsing  
→ Matching  
→ Storage  
→ Telegram Notification

## Tech Stack

### Backend
- Python
- FastAPI
- Pydantic
- PostgreSQL

### Frontend
- React
- TypeScript

### Other
- pytest
- Telegram Bot API

## Project Structure

- domain/ - core application models
- sources/ - integrations with ATS platforms and career pages
- parsers/ - job title, location, and skill normalization
- matching/ - vacancy matching and filtering
- services/ - application workflows
- frontend/ - web interface

## Current Status

The project is currently under development.

Implemented:
- Core Company, RawJob, and Job models
- Greenhouse job collection
- Greenhouse data normalization into a common RawJob format
- Basic React frontend

Currently working on:
- Job title parsing and normalization

## Roadmap

- [x] Define core domain models
- [x] Implement first ATS integration (Greenhouse)
- [x] Normalize Greenhouse vacancies into RawJob
- [ ] Implement title parser
- [ ] Implement location parser
- [ ] Implement skill extraction
- [ ] Implement vacancy matching
- [ ] Add PostgreSQL persistence
- [ ] Add additional ATS sources
- [ ] Add scheduled job collection
- [ ] Add Telegram notifications
- [ ] Connect backend API with frontend
- [ ] Add optional AI-assisted analysis