# AI Research Assistant Architecture
## day 3
User
↓
Persona Selection
(DSA Mentor / Career Coach / GenAI Mentor)
↓
Prompt Builder
↓
Gemini API
↓
Gemini Model
↓
Response
↓
User

# Day 4

```
                           User
                             │
                             ▼
                    Choose Persona
                             │
                             ▼
                    AI Research Assistant
                             │
                             ▼
                   Question Analyzer
                             │
                ┌────────────┴────────────┐
                │                         │
     Starts with "calculate"?            No
                │                         │
               Yes                        ▼
                │                  Gemini API
                ▼                         │
        Calculator Tool                   │
                │                         │
                └────────────┬────────────┘
                             ▼
                      Final Response
                             │
                             ▼
                           User
```


