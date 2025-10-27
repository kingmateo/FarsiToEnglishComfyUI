import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "AHYVFX.TelegramLink",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "Farsi_To_En_offline" || nodeData.name === "Farsi_To_En_DeepSeek") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                const r = onNodeCreated ? onNodeCreated.apply(this, arguments) : undefined;
                
                // اضافه کردن لینک تلگرام به عنوان ویدجت
                this.addWidget(
                    "text",
                    "Telegram",
                    "https://t.me/AHYVFX",
                    function (v) {
                        // وقتی روی لینک کلیک شد
                        window.open("https://t.me/AHYVFX", "_blank");
                    },
                    {
                        serialize: false
                    }
                );
                
                // یا اضافه کردن به عنوان متن ساده قابل کلیک
                this.addWidget(
                    "text",
                    "Developer: AHYVFX",
                    "Click to open Telegram",
                    function (v) {
                        window.open("https://t.me/AHYVFX", "_blank");
                    }
                );
                
                return r;
            };
        }
    },
});