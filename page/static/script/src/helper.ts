class state {
    state: boolean = false;

    toggle(
        override: boolean = null
    ): void {
        if (this.state == null) this.state = false;

        if (override == null) this.state = !this.state;
        else this.state = override;
    }
}

export { state };