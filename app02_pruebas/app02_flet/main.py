import time
import flet as ft 

def main(page: ft.Page):
    t=ft.Text(value="Hola,Flet",color="green")
    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C"),
            ft.Text(t.value)
        ])
    )
    
    for i in range(10):
        t.value=f"Step {i}"
    page.update()
    time.sleep(1)
    
ft.app(target=main)