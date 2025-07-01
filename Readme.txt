
### Explanation
1. **Installation**:
   - Provides steps to clone the repo and install dependencies using `requirements.txt`, matching the template.

2. **Run the Application**:
   - Instructions to start the server with Uvicorn, noting the automatic database creation.

3. **Access API Documentation**:
   - Points to the Swagger UI at `/docs`, a key feature of FastAPI.

4. **Example API Calls**:
   - Includes a variety of `curl` commands for all major endpoints, using the template format. These examples align with your implemented routes (e.g., `/tasks`, `/tasks/{task_id}`).

5. **Seed Sample Data**:
   - Adds instructions for the optional `seed_data.py` script we discussed, enhancing usability.

6. **API Endpoints Overview**:
   - Lists all endpoints with brief descriptions, reflecting the functionality in `routes/tasks.py`.

7. **Notes**:
   - Highlights the SQLite database and prefix structure for clarity.

8. **Contributing and License**:
   - Optional sections for community engagement and legal clarity, which you can customize.

### Integration
- Place this file in the root of your `task-management-api` directory.
- Commit and push it to your GitHub repository:
  ```bash
  git add README.md
  git commit -m "Add README.md with setup and usage instructions"
  git push origin main