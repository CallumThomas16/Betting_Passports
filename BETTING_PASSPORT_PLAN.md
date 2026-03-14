# Betting Passport Development Plan

## Current State Analysis

### Existing Data Assets
- **Normal betting data** (`normal_betting_behaviour.csv`) - 45K rows of normal user behavior
- **Anomalous betting data** (`betting_behaviour_with_anomalies.csv`) - 49K rows with anomaly patterns
- **Small test dataset** (`small_test_dataset.csv`) - 602 rows for testing

### Current Model Infrastructure
- **Single autoencoder model** trained on normal data for anomaly detection
- **8 behavioral features**:
  - `daily_stake` - Amount wagered daily
  - `num_bets` - Number of bets placed
  - `login_hour` - Hour of login
  - `session_duration_mins` - Session length in minutes
  - `days_since_deposit` - Days since last deposit
  - `new_device` - Binary flag for new device usage
  - `foreign_ip` - Binary flag for foreign IP access
  - `anomaly_type` - Type of anomaly (in anomalous dataset)

## Phase 1: Multi-Model Training System

### 1.1 Specialized Model Types

#### Daily Stake Model
- **Purpose**: Analyze daily betting amount patterns
- **Architecture**: Autoencoder
- **Training Data**: `daily_stake` column from all CSV files
- **Output**: Reconstruction error scores for daily stake anomalies

#### Number of Bets Model
- **Purpose**: Detect anomalies in betting frequency
- **Architecture**: Autoencoder
- **Training Data**: `num_bets` column from all CSV files
- **Output**: Pattern recognition for betting frequency anomalies

#### Login Hour Model
- **Purpose**: Identify unusual login time patterns
- **Architecture**: Autoencoder
- **Training Data**: `login_hour` column from all CSV files
- **Output**: Anomaly detection for login time deviations

#### Session Duration Model
- **Purpose**: Detect abnormal session length patterns
- **Architecture**: Autoencoder
- **Training Data**: `session_duration_mins` column from all CSV files
- **Output**: Pattern recognition for session duration anomalies

#### Days Since Deposit Model
- **Purpose**: Analyze deposit timing patterns
- **Architecture**: Autoencoder
- **Training Data**: `days_since_deposit` column from all CSV files
- **Output**: Anomaly detection for deposit timing irregularities

#### New Device Model
- **Purpose**: Detect new device usage patterns
- **Architecture**: Autoencoder
- **Training Data**: `new_device` column from all CSV files
- **Output**: Pattern recognition for device change anomalies

#### Foreign IP Model
- **Purpose**: Identify foreign IP access patterns
- **Architecture**: Autoencoder
- **Training Data**: `foreign_ip` column from all CSV files
- **Output**: Anomaly detection for geographic access irregularities

### 1.2 Modular Training Infrastructure

#### Model Registry System
```python
class ModelRegistry:
    - register_model(name, model, metadata)
    - load_model(name)
    - list_available_models()
    - get_model_info(name)
```

#### Base Trainer Class
```python
class BaseModelTrainer:
    - load_data()
    - preprocess()
    - train()
    - evaluate()
    - save_model()
```

## Phase 2: LangChain Agent Architecture

### 2.1 Model Tools Creation

#### Daily Stake Analysis Tool
- **Input**: User daily stake data
- **Output**: Daily stake anomaly scores and patterns
- **Model Used**: Daily Stake Model

#### Betting Frequency Tool
- **Input**: User number of bets data
- **Output**: Betting frequency anomaly detection
- **Model Used**: Number of Bets Model

#### Login Pattern Tool
- **Input**: User login hour data
- **Output**: Login time anomaly detection
- **Model Used**: Login Hour Model

#### Session Analysis Tool
- **Input**: User session duration data
- **Output**: Session length anomaly detection
- **Model Used**: Session Duration Model

#### Deposit Timing Tool
- **Input**: User days since deposit data
- **Output**: Deposit timing anomaly detection
- **Model Used**: Days Since Deposit Model

#### Device Analysis Tool
- **Input**: User new device usage data
- **Output**: Device change anomaly detection
- **Model Used**: New Device Model

#### Geographic Access Tool
- **Input**: User foreign IP access data
- **Output**: Geographic access anomaly detection
- **Model Used**: Foreign IP Model

### 2.2 Betting Passport Agent

#### Agent Capabilities
- **Orchestration**: Coordinate multiple model tools
- **Decision Making**: Combine insights from different models
- **Explanation**: Provide reasoning for passport decisions
- **User Interaction**: Handle queries about passport results

#### Agent Workflow
1. **Data Ingestion**: Receive user betting data
2. **Model Execution**: Run all relevant model tools
3. **Result Aggregation**: Combine model outputs
4. **Passport Generation**: Create structured betting passport
5. **Explanation Generation**: Provide insights and recommendations

## Phase 3: Unified Interface & Passport System

### 3.1 Betting Passport Structure

#### Passport Sections
- **User Profile**: Basic user information and statistics
- **Risk Assessment**: Overall risk score and breakdown
- **Anomaly History**: Detected anomalies and classifications
- **Behavioral Patterns**: Normal vs. anomalous behavior patterns
- **Temporal Analysis**: Time-based betting insights
- **Recommendations**: Personalized suggestions and flags

#### Passport Formats
- **JSON**: Machine-readable format for APIs
- **PDF**: Human-readable report format
- **HTML**: Interactive web format

### 3.2 API Interface

#### Endpoints
- `POST /passport/generate` - Generate betting passport for user
- `GET /passport/{user_id}` - Retrieve existing passport
- `POST /analyze` - Run specific model analysis
- `GET /models/status` - Check model availability and health

#### Response Schema
```json
{
  "user_id": "string",
  "passport_id": "string",
  "generated_at": "timestamp",
  "risk_score": {
    "overall": "float",
    "level": "string",
    "factors": ["string"]
  },
  "anomalies": [
    {
      "type": "string",
      "severity": "string",
      "confidence": "float",
      "description": "string"
    }
  ],
  "patterns": {
    "normal": ["string"],
    "anomalous": ["string"]
  },
  "recommendations": ["string"]
}
```

## Implementation Timeline

### Week 1: Model Training Infrastructure
- [ ] Refactor existing `model_trainer.py`
- [ ] Create base trainer classes
- [ ] Implement model registry
- [ ] Train specialized models

### Week 2: LangChain Integration
- [ ] Create model tool wrappers
- [ ] Implement betting passport agent
- [ ] Test agent orchestration
- [ ] Create explanation system

### Week 3: Passport Generation
- [ ] Design passport structure
- [ ] Implement generation logic
- [ ] Create export formats
- [ ] Build API interface

### Week 4: Testing & Refinement
- [ ] End-to-end testing
- [ ] Performance optimization
- [ ] Documentation
- [ ] Deployment preparation

## Technical Requirements

### Dependencies
- **Machine Learning**: scikit-learn, pyod
- **LangChain**: langchain, langchain-openai
- **Data Processing**: pandas, numpy
- **API**: fastapi, uvicorn
- **Export**: reportlab (PDF), jinja2 (HTML)

### Infrastructure
- **Model Storage**: Local file system or cloud storage
- **Caching**: Redis for model predictions
- **Logging**: Structured logging for monitoring
- **Configuration**: Environment-based config management

## Success Metrics

### Model Performance
- **Anomaly Detection**: >95% precision, >90% recall
- **Risk Assessment**: >85% accuracy in risk classification
- **Pattern Analysis**: >80% accuracy in temporal pattern detection

### System Performance
- **Response Time**: <5 seconds for passport generation
- **Throughput**: >100 passports per minute
- **Availability**: >99% uptime

### User Experience
- **Interpretability**: Clear explanations for all decisions
- **Actionability**: Specific recommendations for each risk level
- **Usability**: Simple API and clear documentation

## Next Steps

1. **Confirm Requirements**: Validate plan with stakeholders
2. **Environment Setup**: Prepare development environment
3. **Data Validation**: Verify data quality and completeness
4. **Model Development**: Begin with normal behavior model refinement
5. **Iterative Development**: Implement and test each component sequentially
