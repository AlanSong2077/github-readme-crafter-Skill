# Mermaid 图表示例

## 系统架构图

### 微服务架构

```mermaid
flowchart TB
    classDef client fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef gateway fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef service fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef database fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    
    User[User Browser]:::client
    LB[Load Balancer]:::gateway
    API[API Gateway]:::gateway
    
    subgraph Services[Microservices]
        Auth[Auth Service]:::service
        UserSvc[User Service]:::service
        Order[Order Service]:::service
        Payment[Payment Service]:::service
    end
    
    subgraph DataLayer[Data Layer]
        Redis[(Redis Cache)]:::database
        PostgreSQL[(PostgreSQL)]:::database
        MongoDB[(MongoDB)]:::database
    end
    
    User --> LB
    LB --> API
    API --> Auth
    API --> UserSvc
    API --> Order
    Order --> Payment
    
    Auth --> Redis
    UserSvc --> PostgreSQL
    Order --> MongoDB
```

## 技术栈层次图

### Full-Stack Web App

```mermaid
flowchart TB
    subgraph Frontend[Frontend Layer]
        direction TB
        Next[Next.js 14]
        React[React Server Components]
        Tailwind[Tailwind CSS]
        Shadcn[shadcn/ui]
    end
    
    subgraph Backend[Backend Layer]
        direction TB
        Node[Node.js]
        TRPC[tRPC]
        Prisma[Prisma ORM]
    end
    
    subgraph Data[Data Layer]
        direction TB
        Postgres[(PostgreSQL)]
        Redis[(Redis)]
    end
    
    subgraph Infrastructure[Infrastructure]
        direction TB
        Docker[Docker]
        K8s[Kubernetes]
        Vercel[Vercel Edge]
    end
    
    Frontend --> Backend
    Backend --> Data
    Backend --> Infrastructure
```

## 工作流程图

### CI/CD Pipeline

```mermaid
flowchart LR
    A[Code Commit] --> B{Lint & Test}
    B -->|Pass| C[Build]
    B -->|Fail| D[Fix Issues]
    D --> A
    C --> E[Deploy to Staging]
    E --> F{E2E Tests}
    F -->|Pass| G[Deploy to Production]
    F -->|Fail| H[Debug]
    H --> A
```

### 开发流程

```mermaid
flowchart TD
    A[Feature Request] --> B{Planning}
    B --> C[Design]
    C --> D[Implementation]
    D --> E[Code Review]
    E -->|Approved| F[Testing]
    E -->|Changes| D
    F -->|Pass| G[Merge]
    F -->|Fail| D
    G --> H[Release]
```

## 模块依赖图

### Clean Architecture

```mermaid
flowchart TD
    subgraph Presentation[Presentation Layer]
        UI[UI Components]
        Controllers[Controllers]
    end
    
    subgraph Domain[Domain Layer]
        Entities[Entities]
        UseCases[Use Cases]
        Repositories[Repository Interfaces]
    end
    
    subgraph Data[Data Layer]
        Models[Data Models]
        DataRepos[Repository Implementations]
        APIs[API Clients]
    end
    
    UI --> Controllers
    Controllers --> UseCases
    UseCases --> Entities
    UseCases --> Repositories
    DataRepos -.implements.-> Repositories
    DataRepos --> Models
    DataRepos --> APIs
```

## 时序图

### API Request Flow

```mermaid
sequenceDiagram
    participant Client
    participant Gateway
    participant Auth
    participant Service
    participant Database
    
    Client->>Gateway: Request with JWT
    Gateway->>Auth: Validate Token
    Auth-->>Gateway: Token Valid
    Gateway->>Service: Forward Request
    Service->>Database: Query Data
    Database-->>Service: Return Data
    Service-->>Gateway: Processed Response
    Gateway-->>Client: JSON Response
```

## 时间线图

### Project Roadmap

```mermaid
timeline
    title Project Roadmap 2024
    
    Q1 : Project Kickoff
        : Architecture Design
        : MVP Development
        
    Q2 : Beta Release
        : User Testing
        : Performance Optimization
        
    Q3 : v1.0 Release
        : Documentation
        : Community Building
        
    Q4 : v2.0 Planning
        : Feature Expansion
        : Enterprise Support
```

## Git 分支策略

```mermaid
flowchart LR
    subgraph Production
        Main[main]
    end
    
    subgraph Development
        Dev[develop]
    end
    
    subgraph Features
        F1[feature/auth]
        F2[feature/api]
        F3[feature/ui]
    end
    
    subgraph Releases
        R1[release/v1.0]
        R2[release/v1.1]
    end
    
    F1 --> Dev
    F2 --> Dev
    F3 --> Dev
    Dev --> R1
    R1 --> Main
    Dev --> R2
    R2 --> Main
```

## 颜色规范

建议的颜色方案（使用classDef）：

| 类型 | 背景色 | 边框色 | 用途 |
|------|--------|--------|------|
| Client | #e1f5fe | #01579b | 客户端/浏览器 |
| Service | #f3e5f5 | #4a148c | 服务端 |
| Database | #e8f5e9 | #1b5e20 | 数据库 |
| External | #fff3e0 | #e65100 | 外部服务 |
| Queue | #fce4ec | #880e4f | 消息队列 |
| Cache | #f1f8e9 | #33691e | 缓存层 |
