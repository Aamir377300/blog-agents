import sys
import os
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from utils.config import validate_config
from graph.workflow import run_workflow


def display_welcome_banner():
    
    print(" MULTI-AGENT BLOG POST GENERATOR")
    print("Powered by LangChain + LangGraph + Groq")
    
    print("\nThis system uses 4 AI agents working together:")
    print("Agent 1 🔍 Researcher  - Gathers information about your topic")
    print("Agent 2 📋 Outliner    - Creates a structured blog outline")
    print("Agent 3 ✍️  Writer      - Writes the complete blog post")
    print("Agent 4 🔎 Reviewer    - Polishes and improves the content")


def get_user_topic() -> str:
    print("\n📝 STEP 1: Enter Your Blog Topic")
    
    print("Examples:")
    print("  - 'The benefits of remote work'")
    print("  - 'How to learn Python programming'")
    print("  - 'Artificial intelligence in healthcare'")
    print("  - 'Sustainable living tips for beginners'")
    print()

    while True:
        topic = input("Enter your blog topic: ").strip()
        if topic:
            print(f"\n✅ Topic received: '{topic}'")
            return topic
        else:
            print("❌ Please enter a topic. It cannot be empty.")


def save_output_to_file(topic: str, final_content: str) -> str:
    safe_topic = topic.replace(" ", "_")
    safe_topic = "".join(char for char in safe_topic if char.isalnum() or char == "_")
    safe_topic = safe_topic[:30]
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"blog_post_{safe_topic}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"BLOG POST: {topic}\n")
        file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        file.write("="*60 + "\n\n")
        file.write(final_content)

    return filename


def display_final_output(result: dict, topic: str):
    
    print("  🎉 BLOG POST GENERATION COMPLETE!")
    

    if result.get("error_message"):
        print(f"\n❌ An error occurred: {result['error_message']}")
        return

    print("\n" + "📄 FINAL BLOG POST:")
    
    print(result.get("final_content", "No content generated"))
    

    final_content = result.get("final_content", "")
    if final_content:
        filename = save_output_to_file(topic, final_content)
        print(f"\n💾 Blog post saved to: {filename}")

    print("\n" + "-"*65)
    print("Would you like to see the intermediate outputs?")
    print("  1. Research Notes (from Agent 1)")
    print("  2. Blog Outline (from Agent 2)")
    print("  3. Original Draft (from Agent 3)")
    print("  4. No thanks, I'm done")

    choice = input("\nEnter choice (1/2/3/4): ").strip()

    if choice == "1":
        
        print("🔍 RESEARCH NOTES (Agent 1 Output):")
        
        print(result.get("research_notes", "Not available"))
    elif choice == "2":
        
        print("📋 BLOG OUTLINE (Agent 2 Output):")
        
        print(result.get("outline", "Not available"))
    elif choice == "3":
        
        print("✍️  ORIGINAL DRAFT (Agent 3 Output):")
        
        print(result.get("draft_content", "Not available"))
    else:
        print("\n👋 Thanks for using the Multi-Agent Blog Post Generator!")


def main():
    display_welcome_banner()

    print("\n🔧 Checking configuration...")
    try:
        validate_config()
    except ValueError as error:
        print(f"\n{error}")
        print("\nPlease fix the configuration and try again.")
        sys.exit(1)

    topic = get_user_topic()

    
    print("🚀 STARTING MULTI-AGENT WORKFLOW")
    
    print("Please wait while the 4 agents work on your blog post...")
    print("(This typically takes 30-60 seconds)\n")

    try:
        result = run_workflow(topic)
    except Exception as error:
        print(f"\n❌ An unexpected error occurred: {error}")
        print("\nPossible causes:")
        print("  - Invalid or expired Groq API key")
        print("  - No internet connection")
        print("  - Groq API rate limit reached")
        print("\nPlease check the error above and try again.")
        sys.exit(1)

    display_final_output(result, topic)

    print("\n" + "-"*65)
    another = input("Generate another blog post? (yes/no): ").strip().lower()
    if another in ["yes", "y"]:
        main()
    else:
        print("\n👋 Goodbye! Your blog posts have been saved.")


if __name__ == "__main__":
    main()
