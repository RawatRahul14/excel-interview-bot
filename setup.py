# === Python Modules ===
import setuptools

# === Long Description from README ===
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# === Project Metadata ===
__version__ = "0.0.0"
REPO_NAME = "excel-interview-bot"
AUTHOR_USER_NAME = "RawatRahul14"
SRC_REPO = "interviewBot"
AUTHOR_EMAIL = "rahulrawat272chd@gmail.com"

# === Setup Configuration ===
setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "AI-powered Excel Mock Interviewer that conducts structured interviews, evaluates candidate responses, and generates feedback reports.",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)