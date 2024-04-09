LiteGraph.registerNodeType("custom/select", {
    title: "Select",
    init: function() {
        this.addOutput("value", "string");
        this.properties = { value: "Option 1" };
    },
    onDrawBackground: function(ctx) {
        ctx.fillStyle = "#222";
        ctx.fillRect(0, 0, this.size[0], this.size[1]);
    },
    onDrawForeground: function(ctx) {
        ctx.fillStyle = "#fff";
        ctx.fillText(this.properties.value, 10, 20);
    },
    onConfigure: function() {
        this.addWidget("combo", "Value", this.properties.value, function(v) { this.properties.value = v; }, { values: ["Option 1", "Option 2", "Option 3"] });
    },
    onExecute: function() {
        this.setOutputData(0, this.properties.value);
    }
});