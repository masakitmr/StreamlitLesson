import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')
st.write('DataFrame')

df=pd.DataFrame({
  '1列目' :[1 ,2 ,3 ,4],
  '2列目' :[10,20,30,40]
})

st.write(df)
st.dataframe(df.style.highlight_max(axis=0),width=500,height=0)
st.table(df.style.highlight_max(axis=0))

"""
# 見出し1
## 見出し2
### 見出し3

```python
 import streamlit as st
 import numpy as np
 import pandas as pd
```
"""