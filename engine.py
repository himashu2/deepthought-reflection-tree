import json
import os






class ReflectionEngine:
    def __init__(self, json_path):
        self.data = self.load_json(json_path)
        self.nodes = self.data["nodes"]
        self.state = {
            "answers": {},
            "signals": {
                "axis1:internal": 0,
                "axis1:external": 0,
                "axis2:contribution": 0,
                "axis2:entitlement": 0,
                "axis3:self": 0,
                "axis3:others": 0
            }
        }

    def load_json(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"JSON file not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def run(self):
        current = "START"

        while current:
            node = self.nodes[current]
            node_type = node["type"]

            print("\n" + "-" * 60)

            if "message" in node:
                print(self.format_text(node["message"]))

            if node_type == "start":
                input("\nPress Enter to continue...")
                current = node["next"]

            elif node_type == "question":
                selected = self.handle_question(node)
                self.state["answers"][node["id"]] = selected["text"]

                if "signal" in selected:
                    self.state["signals"][selected["signal"]] += 1

                current = node["next"]

            elif node_type == "decision":
                current = self.handle_decision(node)

            elif node_type == "reflection":
                input("\nPress Enter to continue...")
                current = node["next"]

            elif node_type == "bridge":
                input("\nPress Enter to continue...")
                current = node["next"]

            elif node_type == "summary":
                self.print_summary(node)
                input("\nPress Enter to finish...")
                current = node["next"]

            elif node_type == "end":
                print("\n--- End ---")
                break

            else:
                raise Exception(f"Unknown node type: {node_type}")

    # -------------------------
    # QUESTION HANDLER
    # -------------------------
    def handle_question(self, node):
        options = node["options"]

        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt['text']}")

        while True:
            try:
                choice = int(input("\nSelect option: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
            except:
                pass
            print("Invalid input. Try again.")

    # -------------------------
    # DECISION HANDLER
    # -------------------------
    def handle_decision(self, node):
        routing = node.get("routing", {})

        signals = self.state["signals"]

        # Axis 1
        axis1_internal = signals["axis1:internal"]
        axis1_external = signals["axis1:external"]

        # Axis 2
        axis2_contribution = signals["axis2:contribution"]
        axis2_entitlement = signals["axis2:entitlement"]

        # Axis 3
        axis3_self = signals["axis3:self"]
        axis3_others = signals["axis3:others"]

        # ---- LOGIC ----

        if "2x_external" in routing or "2x_internal" in routing:
            if axis1_external >= 2:
                return routing["2x_external"]
            elif axis1_internal >= 2:
                return routing["2x_internal"]
            else:
                return routing["mixed"]

        if "dominant_external" in routing:
            if axis1_external > axis1_internal:
                return routing["dominant_external"]
            elif axis1_internal > axis1_external:
                return routing["dominant_internal"]
            else:
                return routing["mixed"]

        if "dominant_entitlement" in routing:
            if axis2_entitlement > axis2_contribution:
                return routing["dominant_entitlement"]
            elif axis2_contribution > axis2_entitlement:
                return routing["dominant_contribution"]
            else:
                return routing["mixed"]

        if "dominant_self" in routing:
            if axis3_self > axis3_others:
                return routing["dominant_self"]
            elif axis3_others > axis3_self:
                return routing["dominant_others"]
            else:
                return routing["mixed"]

        # fallback
        return node.get("next")

    # -------------------------
    # TEXT FORMATTER
    # -------------------------
    def format_text(self, text):
        for key, value in self.state["answers"].items():
            placeholder = f"{{{key}.answer}}"
            text = text.replace(placeholder, value)
        return text

    # -------------------------
    # SUMMARY
    # -------------------------
    def print_summary(self, node):
        text = self.format_text(node["message"])
        signals = self.state["signals"]

        axis1 = self.get_axis1_summary(signals)
        axis2 = self.get_axis2_summary(signals)
        axis3 = self.get_axis3_summary(signals)

        text = text.replace("{axis1_summary}", axis1)
        text = text.replace("{axis2_summary}", axis2)
        text = text.replace("{axis3_summary}", axis3)

        print(text)

    def get_axis1_summary(self, s):
        if s["axis1:internal"] > s["axis1:external"]:
            return "You mostly held agency — owned what happened."
        elif s["axis1:external"] > s["axis1:internal"]:
            return "Things felt like they were happening to you."
        else:
            return "A mix of ownership and external pressure."

    def get_axis2_summary(self, s):
        if s["axis2:contribution"] > s["axis2:entitlement"]:
            return "You focused on contribution and impact."
        elif s["axis2:entitlement"] > s["axis2:contribution"]:
            return "You were tracking fairness and expectations."
        else:
            return "You balanced contribution and expectations."

    def get_axis3_summary(self, s):
        if s["axis3:others"] > s["axis3:self"]:
            return "You kept others in your frame."
        elif s["axis3:self"] > s["axis3:others"]:
            return "You stayed focused on your own work."
        else:
            return "Your focus shifted between self and others."


# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    import os

    BASE_DIR = os.path.dirname(__file__)
    json_path = os.path.join(BASE_DIR, "reflection-tree.json")

    engine = ReflectionEngine(json_path)
    engine.run()
