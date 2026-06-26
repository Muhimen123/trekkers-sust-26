

## Setup

### Prerequisites

* Python 3.10+
* Git

### Clone the Repository

```bash
git clone <repository-url>
cd trekkers-sust-26
```

### Create and Activate a Virtual Environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

The following sections will be included below:

* Sample Request
* Sample Response
* AI / Model Usage
* Safety Logic
* Limitations
