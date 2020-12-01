class state {
    constructor() {
        this.state = false;
    }
    toggle(override = null) {
        if (this.state == null)
            this.state = false;
        if (override == null)
            this.state = !this.state;
        else
            this.state = override;
    }
}
export { state };
