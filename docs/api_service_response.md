API Service Response规范
------------------------

## 1. json序列化

### 1.1 json
服务通信使用HTTP协议，返回一个json（Content-Type：application/json）格式响应。

json参考：<http://www.json.org/>

### 1.2 序列化

由框架进行序列化，而业务代码需要返回一个可序列化对象。

- 序列化： 将数据结构或对象转换成二进制串的过程。
- 反序列化：将在序列化过程中所生成的二进制串转换成数据结构或者对象的过程。

以python为例，使用标准库`json`操作。`json.dumps()`把python dict对象序列化成json字符串，`json.loads()`把json字符串反序列化成python dict对象。


## 2. 格式

一个典型的response：
```
HTTP状态码：200

HTTP响应体：
{
  "data": {
    "ship_infos": {}
  },
  "code": 200,
  "innerErrMsg": "",
  "errMsg": ""
}
```
如上例，除非发生web server级错误，HTTP状态码**永远**为200。

成功响应：code为200或500
失败响应：code为404或531

- code:表示该请求的执行结果，200或500由业务代码提供，其他由框架捕捉。
	- 200：业务成功（业务标识）
	- 500：业务失败（业务标识）
	- 531：发生未捕获异常（框架添加标识）
	- 404：找不到相应资源（框架添加标识，类似于HTTP 404）
- data:具体的业务数据，在失败响应，无此字段。
- innerErrMsg：当发生失败响应，内容为堆栈信息，否则为空字符串。
- errMsg：错误信息。在非面向最终用户的服务中，此内容无实际意义，可为空。在面向最终用户的服务中，errMsg为用户可见的信息。



**注**：

1. **提示信息**：面向最终用户的文字提示。
	- 提示信息的产生方，即具体处理业务逻辑的代码。
	- 提示信息的展示方，即把提示信息展现给最终用户的服务。
	- 提示信息的传输方，即产生方、展示方中间的服务。
	**要求**产生方给出能确定信息的可供代码处理的参数（如type），由展示方解析成文字描述，而传输方只传递参数。如：
		在微众卡查询的业务中，用户会得到“卡号或密码错误”这样的信息，card_apiserver产生类型"wzcard:aaa",apiserver传递给h5,h5根据需求生成文字。因为产品需求瞬息万变，信息文字可能随时变化，则只要h5更改；又card_apiserver可能给出"wzcard:nosuch"（表示没有这张卡）和"wzcard:wrongpass"(密码错误)，h5根据产品需求都显示成“卡号或密码错误”。