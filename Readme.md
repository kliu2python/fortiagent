## 📦 Installation - Quick start

install playwright:

```shell
playwright install
```

```bash

pip install -r requirements.txt

Create .env file
Place your GOOGLE_API_KEY=AIzaXXXXXXXXXXXXXX

streamlit run app.py

```

### Frontend

The Streamlit user interface is organized in `src/frontend`. Custom styles live in `src/frontend/styles.css` and are loaded by `src/frontend/ui.py`.

A simple Next.js frontend has been added in the `frontend` directory. It fetches data from the API described below and can be started with:

```bash
cd frontend
npm install
npm run dev
```

### API Backend

An experimental FastAPI backend exposes an OpenAPI specification at `/docs`. Run it with:

```bash
uvicorn backend.main:app --reload
```

### Mobile Testing

A dedicated mobile agent can transform manual iOS and Android test cases into
Gherkin, execute them on real devices or emulators using Appium, and output
PyTest automation code. See `src/Prompts/mobile_prompts.py` for usage examples.
