# Bakery Management System — MVC Architecture

A console-based application developed in Python following the **Model-View-Controller (MVC)** architectural pattern, enforcing strict separation of concerns across components for maintainability, clarity, and scalability.

---

## Features

- Register customers by name, phone, and state.  
- Register products by name, taste, and price.  
- List all registered products.  
- List all registered customers.  
- Search customers by name.  
- Search customers by state.  
- Search products by taste.  
- Display all customers and products.  
- Graceful application exit.

---

## Architecture

This project is structured according to the **MVC (Model-View-Controller)** design pattern. Each component is isolated according to its specific responsibility:

### Model
Responsible for encapsulating domain data and business rules.  
Entities such as `Product` and `Customer` handle:
- Data formatting and normalization (e.g., trimming input, casing, accent removal).
- Internal validation rules (e.g., valid price values, cleaned phone numbers).

### View
Responsible for interacting with the user (input and output).  
Each view is isolated and handles only:
- Collecting user input.
- Displaying information and feedback.

Views do **not** contain logic or coordinate flow. They are invoked and managed by controllers.

### Controller
Orchestrates the application’s behavior by coordinating between Views and Models.  
Responsibilities include:
- Managing flow logic.
- Receiving inputs from views, instantiating models, and delegating to repositories.
- Handling exceptions and sending appropriate feedback to the view.

### Repository (Infrastructure Layer)
Implements database operations using SQLite, abstracted via:
- `ProductRepository`
- `CustomerRepository`

Each repository handles:
- Table creation (if not exists)
- Insertions
- Queries by fields
- Retrieval of all records

---

## Requirements

- Python 3.11 or higher  
- Standard library only (no third-party dependencies)  
- SQLite (`sqlite3` module)

---

## How to Run

```bash
python run.py
```

---

## Design Principles Applied

- **Single Responsibility Principle (SRP)**: Each class has a unique, well-defined responsibility.
- **Separation of Concerns (SoC)**: Views, Controllers, Models, and Repositories are decoupled.
- **Encapsulation**: Models handle their own formatting and validation.
- **Low Coupling / High Cohesion**: Layers are independent and focused.
- **Testability**: With logic centralized and isolated, the codebase is fully testable.

---

## Recommendations for Next Steps

- Add unit and integration tests using `pytest`.
- Refine exception handling and error feedback.
- Introduce data deletion and update features.
- Implement a simple logging mechanism for operations.
- Optionally extend to a web version using FastAPI, preserving the MVC structure.