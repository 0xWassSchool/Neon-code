# **Installation**


> GIT installation

1. git clone https://github.com/0xWasosky/Neon-code.git
2. cd Neon-code
3. pip install -r .\requirements.txt4
4. python3 run.py -> ( python3 setup.py )


# **Plugin**

```python
from pkg import IPlugin, Window


class NewPlugin(IPlugin):
    def __body__(self):
        """
        The body of your plugin 
        >> you can use the Window class for add custom items into the window
        """

def run():
    return NewPlugin().__body__()
```

## How can import my new plugin?

1. python3 main.py 
2. terminal command: load-plugin; new_plugin.py

# **Theme**

```json
{
  "version": "1.0.0",
  "ui": {
    "text-color": "white",
    "background": "#2A2824",
    "font-size": 12,
    "font": "Arial"
  }
}
```

## How can import my new theme?

1. Open APPDATA\\neon_code\\config\\standard.json
2. Insert your json in the json file and save
3. Restart the editor
