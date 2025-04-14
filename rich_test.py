from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.markdown import Markdown
from rich import box

console = Console()

# 1. 감성적인 인사말
greeting = Text()
greeting.append("🌟 환영합니다! ", style="bold magenta")
greeting.append("Rich를 이용한 아름다운 출력 예제입니다.\n", style="italic green")
console.print(greeting)

# 2. 마크다운 텍스트 출력
md = Markdown("""
## 💡 오늘의 주제: Rich 라이브러리

Rich는 **Python CLI 출력**을 아름답게 만들어주는 도구입니다.
아래는 학생 정보를 담은 테이블 예시입니다.
""")
console.print(md)

# 3. 테이블 생성 (아름답게 꾸미기)
table = Table(title="📚 학생 정보 테이블 📚", box=box.ROUNDED, border_style="bright_blue")

table.add_column("이름", justify="center", style="bold cyan", no_wrap=True)
table.add_column("나이", justify="right", style="bold green")
table.add_column("전공", style="bold yellow")

table.add_row("🧑 철수", "20", "컴퓨터공학")
table.add_row("👩 영희", "21", "경영학")
table.add_row("🧑 민수", "22", "심리학")

console.print(table)

# 4. 패널로 마무리
footer = Panel.fit(
    "[bold green]이 예제는 [link=https://gptonline.ai/ko/]GPT 온라인[/link]에서 제공되었습니다![/bold green] 🎉",
    title="감사합니다 🙏",
    subtitle="Rich is beautiful 💖",
    style="bold magenta"
)

console.print(footer)
