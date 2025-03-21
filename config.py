from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
API_URL = os.getenv('API_URL')
API_AUTHORIZATION = os.getenv('API_AUTHORIZATION')

if not TOKEN or not API_URL or not API_AUTHORIZATION:
    raise ValueError("Необходимые переменные окружения не установлены в .env файле")

MODELS = {
    "1": "Qwen/QwQ-32B",
    "2": "meta-llama/Llama-3.2-90B-Vision-Instruct",
    "3": "deepseek-ai/DeepSeek-R1",
    "4": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
    "5": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    "6": "meta-llama/Llama-3.3-70B-Instruct",
    "7": "Qwen/Qwen2-VL-7B-Instruct",
    "8": "databricks/dbrx-instruct",
    "9": "mistralai/Ministral-8B-Instruct-2410",
    "10": "netease-youdao/Confucius-o1-14B",
    "11": "nvidia/AceMath-7B-Instruct",
    "12": "neuralmagic/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-dynamic",
    "13": "mistralai/Mistral-Large-Instruct-2411",
    "14": "microsoft/phi-4",
    "15": "SentientAGI/Dobby-Mini-Unhinged-Llama-3.1-8B",
    "16": "watt-ai/watt-tool-70B",
    "17": "bespokelabs/Bespoke-Stratos-32B",
    "18": "NovaSky-AI/Sky-T1-32B-Preview",
    "19": "tiiuae/Falcon3-10B-Instruct",
    "20": "CohereForAI/c4ai-command-r-plus-08-2024",
    "21": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "22": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "23": "CohereForAI/aya-expanse-32b",
    "24": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "25": "CohereForAI/aya-expanse-32b",
    "26": "jinaai/ReaderLM-v2",
    "27": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "28": "CohereForAI/aya-expanse-32b",
    "29": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "30": "CohereForAI/aya-expanse-32b",
    "31": "jinaai/ReaderLM-v2",
    "32": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "33": "CohereForAI/aya-expanse-32b",
    "34": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "35": "CohereForAI/aya-expanse-32b",
    "36": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "37": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "38": "CohereForAI/aya-expanse-32b",
    "39": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "40": "CohereForAI/aya-expanse-32b",
    "41": "jinaai/ReaderLM-v2",
    "42": "openbmb/MiniCPM3-4B",
    "43": "Qwen/Qwen2.5-1.5B-Instruct",
    "44": "ozone-ai/0x-lite",
    "45": "microsoft/Phi-3.5-mini-instruct",
    "46": "ibm-granite/granite-3.1-8b-instruct"
}

DEFAULT_MODEL = MODELS["1"]

API_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_AUTHORIZATION}",
}