import pyhabitat as ph
from pipeline_eds.security_and_config import SecurityAndConfig as SC
from pipeline_eds.security_and_config import ForcePrompt


print(f"ph.interactive_terminal_is_available() = {ph.interactive_terminal_is_available()}")
print(f"ph.tkinter_is_available() = {ph.tkinter_is_available()}")
print(f"ph.web_browser_is_available() = {ph.web_browser_is_available()}")

SC.prompt_for_value(prompt_message = "prompt_message", force = ForcePrompt.GUI)
