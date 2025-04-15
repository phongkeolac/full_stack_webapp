"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"
    # original_label = "This is my label"
    
    # def change_labels(self):
    #     if self.label == "Cool label.":
    #         self.label = self.original_label
    #     else:
    #         self.label = "Cool label."

    def handle_title_input_change(self, val):
        self.label = val

    def did_click(self):
        print("Hello world did click")


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="bottom-left"),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                # on_click=State.change_labels,
                size="5",
            ),
            rx.input(
                default_value=State.label,
                on_click=State.did_click,
                on_change=State.handle_title_input_change),
            # rx.button("Do somethings!", on_click=State.change_labels),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
