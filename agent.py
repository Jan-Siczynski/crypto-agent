# agent.py
import json
import anthropic
from config import ANTHROPIC_API_KEY
from tools import TOOLS
from coingecko import get_prices, get_trending, get_global_market
from report_generator import save_report

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# Mapowanie: nazwa narzędzia → funkcja Pythona
TOOL_EXECUTOR = {
    "get_crypto_prices":     lambda _: get_prices(),
    "get_trending_coins":    lambda _: get_trending(),
    "get_global_market_data": lambda _: get_global_market(),
    "generate_report":       lambda inp: save_report(inp["report_content"]),
}

SYSTEM_PROMPT = """Jesteś analitykiem rynku kryptowalut.
Twoim zadaniem jest:
1. Pobrać aktualne ceny BTC, ETH, SOL
2. Pobrać trendujące coiny
3. Pobrać globalne dane rynku
4. Na podstawie tych danych wygenerować profesjonalny raport dzienny w Markdown

Raport powinien zawierać: podsumowanie rynku, analizę głównych monet, trendy, krótką prognozę nastrojów."""

def run_agent():
    """Główna pętla agenta z function calling."""
    messages = [
        {"role": "user", "content": "Wygeneruj dzienny raport rynku kryptowalut."}
    ]

    print("🤖 Agent startuje...")

    # Pętla agenta — trwa dopóki LLM nie skończy
    while True:
        response = client.messages.create(
            model="claude-opus-4-6",  # lub claude-sonnet-4-6
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )

        print(f"   Stop reason: {response.stop_reason}")

        # LLM skończył — nie chce już narzędzi
        if response.stop_reason == "end_turn":
            print("✅ Agent zakończył pracę.")
            break

        # LLM chce wywołać narzędzie/a
        if response.stop_reason == "tool_use":
            # Dodaj odpowiedź asystenta do historii
            messages.append({"role": "assistant", "content": response.content})

            tool_results = []
            for block in response.content:
                if block.type != "tool_use":
                    continue

                tool_name = block.name
                tool_input = block.input
                print(f"   🔧 Wywołuję: {tool_name}")

                # Wykonaj narzędzie
                try:
                    result = TOOL_EXECUTOR[tool_name](tool_input)
                    result_str = json.dumps(result, ensure_ascii=False)
                    is_error = False
                except Exception as e:
                    result_str = f"Błąd: {str(e)}"
                    is_error = True

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result_str,
                    "is_error": is_error,
                })

            # Zwróć wyniki narzędzi do LLM
            messages.append({"role": "user", "content": tool_results})

if __name__ == "__main__":
    run_agent()