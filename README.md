<div align="center"><img src="https://raw.githubusercontent.com/macielalves/McCalc/main/img/icon.png" /></div>

---
# McCalc

![PyPI - License](https://img.shields.io/pypi/l/McCalc) ![PyPI - Downloads](https://img.shields.io/pypi/dm/McCalc) ![PyPI - Version](https://img.shields.io/pypi/v/McCalc)

Uma simples calculadora feita em python

* #### Como instalar?
Se seu sistema operacional é debian/ubuntu, use o seguinte comando:

```shell
python3 -m pip install McCalc
```

Para instalar no windows:
```bash
py.exe -m pip install McCalc
```

Após instalar, é preciso criar um arquivo e passar as intruções de uso.

Para usar via terminal:

```py
from McCalc import McCalc

calc1 = McCalc()
calc1.run()
```

Para usar no modo GUI, use o seguinte exemplo:
```py
# O modo interface usa bibliotecas tkinter
from McCalc import CalcGUI

test = CalcGUI()
test.execute()
```



⚠ Pode haver bugs, relate em [issues](https://github.com/macielalves/McCalc/issues/new)
