## FastAPI Side Hustles & Money Quotes API 🚀💡

### Overview 📝
This FastAPI application provides two endpoints:
1. `/side_hustles`: Returns a random side hustle idea 💼.
2. `/money_quotes`: Returns a random motivational quote related to money 💰.

Both endpoints require an API key for authentication 🔑, and they provide different responses based on the request made.

### Installation 🛠️

1. Clone the repository:
    ```bash
    git clone <https://github.com/ersa-rani/SIMPLE-API->
    ```

2. Install the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

### Environment Variables ⚙️
The application uses an API key for authentication 🔑. You need to set up the API key as an environment variable for secure access.

- **FASTAPI_SECRET_KEY**: Set this environment variable to a secret key value, e.g., "1234567890", or replace it with your own key.
  
  You can set the environment variable on Linux/Mac with:
  ```bash
  export FASTAPI_SECRET_KEY="1234567890"
  ```

  On Windows, you can set it with:
  ```bash
  set FASTAPI_SECRET_KEY="1234567890"
  ```

### Endpoints 🚦

1. **GET `/side_hustles`** 🏠💼

   - **Description**: Returns a random side hustle idea from a predefined list.
   - **Parameters**:
     - `api_key` (required): Provide the valid API key as a query parameter 🔑.
   - **Response**:
     ```json
     {
       "side_hustle": "Freelancing - Start offering your skills online! ✍️"
     }
     ```

2. **GET `/money_quotes`** 💬💸

   - **Description**: Returns a random motivational money-related quote.
   - **Parameters**:
     - `api_key` (required): Provide the valid API key as a query parameter 🔑.
   - **Response**:
     ```json
     {
       "money_quote": "The way to get started is to quit talking and begin doing. – Walt Disney 💪"
     }
     ```

### Authentication 🔐
Each request to the endpoints must include a valid `api_key` parameter. The API key is used to authenticate and ensure the security of the application.

- If the API key is incorrect or missing, the response will return a `401 Unauthorized` status code ❌.
  Example:
  ```json
  {
    "detail": "Invalid API key ⚠️"
  }
  ```

### Random Data 🎲

- The **side_hustles** list contains various side hustle ideas, such as:
  - Freelancing ✍️
  - Dropshipping 📦
  - Blogging ✍️
  - Affiliate Marketing 📣
  - And more!

- The **money_quotes** list includes motivational quotes about money from well-known figures, such as:
  - Warren Buffett 💼
  - Jim Rohn 📚
  - Walt Disney 🎢
  - P.T. Barnum 🎩
  - And more!

### Example Requests 💻

1. **Get a random side hustle idea**:
   ```
   GET /side_hustles?api_key=your-api-key
   ```

   Response:
   ```json
   {
     "side_hustle": "Stock Market - Invest and watch your money grow! 📈"
   }
   ```

2. **Get a random money quote**:
   ```
   GET /money_quotes?api_key=your-api-key
   ```

   Response:
   ```json
   {
     "money_quote": "Money grows on the tree of persistence. – Japanese Proverb 🌳"
   }
   ```

### License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

