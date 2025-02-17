# Component Definition

This file defines the components of this project. 

## Characteristics of a Component

*   **Clear Interface:** Each component has a public interface that defines how other components can interact with it.
*   **Testability:** Components are written to be easily testable in isolation, with unit tests covering their core functionality.
*   **Reusability:** Components are designed to be reusable across different parts of the project.

### Calculator Component

The `Calculator` component is responsible for performing basic arithmetic operations, such as addition, subtraction, multiplication, and division.

### Logger Component

The `Logger` component records the operations performed by the `Calculator` component.

### Notifier Component

The `Notifier` component sends an alert when the result of a calculation performed by the `Calculator` component exceeds a given threshold.