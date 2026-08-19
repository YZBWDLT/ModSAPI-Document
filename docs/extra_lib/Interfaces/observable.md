---
sidebar_position: 3
---

# Observable - 可观测变量

## 概述

可观测变量类，用于实现数据双向绑定和响应式编程。当变量值发生变化时，所有订阅的回调函数都会被触发。

## 创建

### create

`create(value: any)`

创建一个表单。

#### 参数

- value: any
  - 变量初值

## 属性

### identifier

`identifier: str`

变量标识符，可以用于区分变量。

## 方法

### getValue

`getValue() -> any`

获取变量的当前值。

#### 参数

无

#### 返回值

- any
  - 变量的当前值。

---

### setValue

`setValue(v) -> None`

设置变量的新值。如果新值与旧值不同，会触发所有订阅的回调函数，并同步更新到服务端或客户端。

#### 参数

- v: any
  - 要设置的新值。

#### 返回值

- None

---

### subscribe

`subscribe(callback) -> None`

订阅变量更新事件。当变量值发生变化时，注册的回调函数会被调用。

**注意：** 触发回调时，变量还未应用更新，可以通过 `getValue()` 获取更新前的旧值。

#### 参数

- callback: Callable[[any], None]
  - 回调函数，参数为更新后的新值。

#### 返回值

- None

---

### unsubscribe

`unsubscribe(callback) -> None`

取消订阅变量更新事件。

#### 参数

- callback: Callable[[any], None]
  - 要取消的回调函数。

#### 返回值

- None

---

## 比较运算符

Observable 支持所有比较运算符，返回一个新的 Observable 对象，用于响应式比较。

| 运算符 | 方法 | 说明 |
|--------|------|------|
| `<` | `__lt__` | 小于比较 |
| `<=` | `__le__` | 小于等于比较 |
| `>` | `__gt__` | 大于比较 |
| `>=` | `__ge__` | 大于等于比较 |
| `==` | `__eq__` | 等于比较 |
| `!=` | `__ne__` | 不等于比较 |

---

## 算术运算符

Observable 支持所有算术运算符，返回一个新的 Observable 对象，用于响应式计算。

| 运算符 | 方法 | 说明 |
|--------|------|------|
| `+` | `__add__` | 加法运算 |
| `-` | `__sub__` | 减法运算 |
| `*` | `__mul__` | 乘法运算 |
| `/` | `__truediv__` | 真除法运算 |
| `//` | `__floordiv__` | 整除运算 |
| `%` | `__mod__` | 取模运算 |
| `**` | `__pow__` | 幂运算 |

---

## 位运算符

Observable 支持所有位运算符，返回一个新的 Observable 对象，用于响应式位运算。

| 运算符 | 方法 | 说明 |
|--------|------|------|
| `&` | `__and__` | 按位与运算 |
| `\|` | `__or__` | 按位或运算 |
| `^` | `__xor__` | 按位异或运算 |
| `<<` | `__lshift__` | 左移运算 |
| `>>` | `__rshift__` | 右移运算 |

---

## 使用示例

### 基础用法

```python
from xxx.xxx import Observable

# 创建 Observable
count = Observable(0, "count")

# 订阅变化
def on_count_changed(new_value):
    print(f"计数从 {count.getValue()} 变为 {new_value}")

count.subscribe(on_count_changed)

# 修改值
count.setValue(10)  # 输出：计数从 0 变为 10
count.setValue(20)  # 输出：计数从 10 变为 20
```

### 响应式计算

```python
# 创建基础变量
price = Observable(100, "price")
quantity = Observable(2, "quantity")

# 响应式计算总价
total = price * quantity
total.subscribe(lambda v: print(f"总价: {v}"))

price.setValue(150)  # 输出：总价: 300
quantity.setValue(3) # 输出：总价: 450
```

### 响应式比较

```python
score = Observable(85, "score")

# 判断是否及格
is_passed = score >= 60
is_passed.subscribe(lambda v: print(f"是否及格: {v}"))

score.setValue(59)  # 输出：是否及格: False
score.setValue(75)  # 输出：是否及格: True
```

### 在表单中使用

```python
from xxx.xxx import Form, Observable

# 创建 Observable 数据
username = Observable("", "username")
age = Observable(18, "age")
is_active = Observable(True, "is_active")

# 在表单中使用
form = Form()
form.textfield("用户名", username)
form.slider("年龄", age, minValue=0, maxValue=120)
form.toggle("激活状态", is_active)

# 监听数据变化
username.subscribe(lambda v: print(f"用户名已更改为: {v}"))
age.subscribe(lambda v: print(f"年龄已更改为: {v}"))
```

### 取消订阅

```python
def callback(new_value):
    print(f"值已更新: {new_value}")

data = Observable(0, "data")
data.subscribe(callback)

data.setValue(10)  # 输出：值已更新: 10

# 取消订阅
data.unsubscribe(callback)
data.setValue(20)  # 无输出
```

---

## 注意事项

1. **旧值访问**：在订阅回调中，`getValue()` 获取的是更新前的旧值。

2. **自动同步**：`setValue` 会自动同步到服务端或客户端，无需手动调用同步方法。

3. **运算符重载**：所有运算符都返回新的 Observable 实例，可以链式组合使用。

4. **性能考虑**：频繁更新 Observable 会触发大量回调，注意控制更新频率。

5. **循环引用**：避免在回调中修改同一个 Observable 导致无限递归。

6. **线程安全**：Observable 操作需要在主线程中执行。