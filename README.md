# Fifa 19 Top 25 Players Analysis
## Overview
This project explores the attributes that make the top 25 players in FIFA 19 stand out in their positions. Using Python, Pandas, and Matplotlib, I analysed player data to identify position-specific skill patterns and trends in player age distribution.

## Data Source
The dataset was obtained from Kaggle and contains detailed attribute data for FIFA 19 players, including overall ratings, age, and position-specific skills.

## Key Questions
What attributes are most important for different positions (Goalkeeper, Defender, Midfielder, Winger, Striker)?

At what age do top players typically peak?

How do skill profiles differ between positions?

## Findings
### Age Distribution
The top 25 players showed a bimodal age distribution, with peaks at 27 and 32 years

Pace-reliant players (wingers, forwards) tend to peak earlier (~27)

Technical/defensive players often peak later (~32)

### Position-Specific Key Attributes
Position	Key Attributes
Goalkeeper	Reflexes, Handling, Diving
Centre Back	Standing Tackle, Jumping, Marking
Central Midfielder	Reactions, Short Passing, Ball Control, Vision
Winger	Dribbling, Ball Control, Agility, Acceleration
Striker	Finishing, Positioning, Reactions, Composure
Notable Insights
Reactions emerged as a critical attribute across almost all positions

Contrary to expectations, crossing was not a top attribute for wingers - suggesting the top players in this dataset function more as inside forwards than traditional wingers

Strikers and wingers share many key attributes, but finishing and positioning are uniquely critical for strikers

## Tools Used
Python: Pandas, NumPy, Matplotlib

Jupyter Notebook: For analysis and reporting

Tableau: For enhanced visualisation

## Files
- top_25_players_analysis.ipynb - Main analysis notebook
- Fifa 19 Data Analysis.pptx - Analysis presentation
- top_25.py - Raw Python code
- data.csv - Source dataset
