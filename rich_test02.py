from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from rich.text import Text
from rich import box  # 테두리 스타일 지정용

console = Console()

def print_cute_ascii_art(choice):
    """선택된 번호에 따라 예쁜 아스키 아트를 중앙에 출력하는 함수"""

    if choice == 1:
        # 원래 고양이 아트 유지
        cat = """
              /\\_/\\
             ( o.o )
              > ^ <
        """
        console.print(
            Align.center(
                Panel(
                    cat,
                    title="🐱 고양이",
                    style="bold magenta",
                    padding=(1, 2),
                    box=box.SQUARE,
                    width=40
                )
            )
        )

    elif choice == 2:
        # 원래 토끼 아트 유지
        rabbit = """
              (\\_/)
             (=';'=)
             (\")_(\")
        """
        console.print(
            Align.center(
                Panel(
                    rabbit,
                    title="🐰 토끼",
                    style="bold deep_pink4",
                    padding=(1, 2),
                    box=box.SQUARE,
                    width=40
                )
            )
        )

    elif choice == 3:
        # 원래 강아지 아트 유지
        dog = """
            __
            o-''|\\_____/)
            \\_/|_)     )
                \\  __  /
                (_/ (_/
        """
        console.print(
            Align.center(
                Panel(
                    dog,
                    title="🐶 강아지",
                    style="bold yellow",
                    padding=(1, 2),
                    box=box.SQUARE,
                    width=40
                )
            )
        )

    else:
        console.print(Align.center("[red]⚠️ 잘못 입력했습니다. 1, 2, 3 중 하나를 입력해주세요.[/red]"))

def main():
    title = Text("🎨 귀여운 아스키 아트 출력기 🎨", style="bold cyan")

    # subtitle을 dim 스타일로 약간 작고 연한 느낌으로 조정
    subtitle = Text("원하는 동물을 고르세요!", style="dim")

    console.print(Align.center(Panel(title, subtitle=subtitle, style="bold blue")))

    console.print()  # 여백 추가 (줄 바꿈)

    menu = Text()
    menu.append("1. 고양이 🐱\n", style="bold magenta")
    menu.append("2. 토끼 🐰\n", style="bold deep_pink4")
    menu.append("3. 강아지 🐶\n", style="bold yellow")
    menu.append("0. 프로그램 종료 ❌\n", style="bold red")

    console.print(Align.center(menu))

    while True:
        try:
            n = int(Prompt.ask("[bold green]선택[/bold green]", default="1"))
            if n == 0:
                console.print(Align.center("\n[bold red]프로그램을 종료합니다. 안녕히 가세요! 👋[/bold red]"))
                break
            print_cute_ascii_art(n)
        except ValueError:
            console.print(Align.center("[red]숫자를 입력해주세요![/red]"))

if __name__ == "__main__":
    main()
