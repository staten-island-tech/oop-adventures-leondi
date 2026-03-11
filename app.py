import tkinter as tk


class Clicker:
    """Holds the state for the clicker game."""

    def __init__(self) -> None:
        # base values
        self.points = 0
        self.mult = 1
        self.autos = 0

    def click(self) -> None:
        """Manually click to earn points."""
        self.points += self.mult

    def multiplier_cost(self) -> int:
        return 10 * self.mult

    def buy_multiplier(self) -> bool:
        """Attempt to purchase a multiplier upgrade.

        Returns True if purchase succeeded, False otherwise.
        """
        cost = self.multiplier_cost()
        if self.points >= cost:
            self.points -= cost
            self.mult += 1
            return True
        return False

    def autoclicker_cost(self) -> int:
        # exponential cost curve
        return 50 * (2 ** self.autos)

    def buy_autoclicker(self) -> bool:
        cost = self.autoclicker_cost()
        if self.points >= cost:
            self.points -= cost
            self.autos += 1
            return True
        return False

    def auto_tick(self) -> None:
        """Called periodically by the GUI to add automatic points."""
        self.points += self.autos * self.mult


class GameWindow:
    """Tkinter window that displays the clicker game."""

    def __init__(self, root: tk.Tk, clicker: Clicker) -> None:
        self.root = root
        self.clicker = clicker

        root.title("Stupid Ahh Clicker Game")
        root.geometry("400x300")
        root.resizable(False, False)

        self.points_var = tk.StringVar()
        self.mult_var = tk.StringVar()
        self.autos_var = tk.StringVar()

        self._build_ui()
        self._update_labels()
        # schedule the auto clicker to tick every second
        root.after(1000, self._auto_tick)

    def _build_ui(self) -> None:
        lbl = tk.Label(self.root, textvariable=self.points_var, font=("Helvetica", 16))
        lbl.pack(pady=10)

        click_btn = tk.Button(self.root, text="Click!", command=self._on_click, width=20)
        click_btn.pack(pady=5)

        mult_btn = tk.Button(
            self.root,
            text="Buy Multiplier",
            command=self._on_buy_multiplier,
            width=20,
        )
        mult_btn.pack(pady=5)

        auto_btn = tk.Button(
            self.root,
            text="Buy Autoclicker",
            command=self._on_buy_autoclicker,
            width=20,
        )
        auto_btn.pack(pady=5)

        # show current stats
        tk.Label(self.root, textvariable=self.mult_var).pack(pady=2)
        tk.Label(self.root, textvariable=self.autos_var).pack(pady=2)

    def _update_labels(self) -> None:
        self.points_var.set(f"Points: {self.clicker.points}")
        self.mult_var.set(f"Multiplier: x{self.clicker.mult} (cost {self.clicker.multiplier_cost()})")
        self.autos_var.set(
            f"Autoclickers: {self.clicker.autos} (cost {self.clicker.autoclicker_cost()})"
        )

    def _on_click(self) -> None:
        self.clicker.click()
        self._update_labels()

    def _on_buy_multiplier(self) -> None:
        if self.clicker.buy_multiplier():
            self._update_labels()

    def _on_buy_autoclicker(self) -> None:
        if self.clicker.buy_autoclicker():
            self._update_labels()

    def _auto_tick(self) -> None:
        self.clicker.auto_tick()
        self._update_labels()
        self.root.after(1000, self._auto_tick)


if __name__ == "__main__":
    root = tk.Tk()
    game = Clicker()
    GameWindow(root, game)
    root.mainloop()
