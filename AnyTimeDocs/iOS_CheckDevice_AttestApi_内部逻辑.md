


# 总结

CheckDevie API 和 Attest API 是用于校验 app 的完整性，和 app 内用户数据的留存；

都是通过在客户端拿到一个字符串，然后去服务端调 Apple 的接口；

CheckDevie 主要返回的是标识位，目前看到的是一个布尔值；

Attest API 是判断 app 是否被篡改，是否为重打包；

这两个接口都需要去苹果开发者后台申请：PRIVATE_KEY_ID、YOUR_TEAM_ID、YOUR_PRIVATE_KEY 


# 1

# iOS DeviceCheck 使用示例

#### You:
如何使用 iOS DeviceCheck 功能，给我详细的步骤描述和具体的示例代码

#### ChatGPT:
在iOS应用程序中，Apple提供了一种称为DeviceCheck的功能，允许开发者在服务器和苹果设备之间生成和共享一个唯一的设备标识符，这个标识符与用户的Apple ID、设备信息或其他APP之间没有任何关联。这种机制允许应用程序在保护用户隐私的同时，追踪设备的行为。

以下是使用DeviceCheck功能的详细步骤：

1. **在您的iOS应用程序中集成DeviceCheck框架**

在项目中，您需要导入DeviceCheck框架。可以在所需的类中使用以下代码行完成此操作：

```swift
import DeviceCheck
```

2. **生成设备标识符**

在应用程序中，您可以使用DCDevice类的generateToken方法生成设备的标识符。以下是一个示例：

```swift
if DCDevice.current.isSupported {
    DCDevice.current.generateToken(completionHandler: { (data, error) in
        if let tokenData = data {
            // Use the tokenData, send it to the server
        } else if let error = error {
            // Handle the error
        }
    })
}
```

请注意，这种方法只能在真机上运行，而不能在模拟器上运行。

3. **将设备标识符发送到您的服务器**

一旦你有了设备的标识符，你需要把它发送到你的服务器，你的服务器应该保存这个标识符以便以后使用。一般来说，您可以使用如下方法把标识符转换成字符串，然后再发送到服务器：

```swift
let tokenString = tokenData.base64EncodedString()
```

4. **在您的服务器上验证设备标识符**

最后，您需要在服务器上使用苹果的DeviceCheck服务验证设备标识符。您可以通过调用苹果的DeviceCheck API完成这个步骤。以下是一个使用Python发送HTTP POST请求的例子：

```python
import requests
import jwt

# Create the JWT
header = {"alg": "ES256", "kid": "YOUR_PRIVATE_KEY_ID"}
payload = {"iss": "YOUR_TEAM_ID", "iat": "YOUR_TIMESTAMP"}
private_key = "YOUR_PRIVATE_KEY"
token = jwt.encode(payload, private_key, algorithm='ES256', headers=header)

# Send the request
headers = {"Authorization": f"Bearer {token}"}
data = {"device_token": "DEVICE_TOKEN", "transaction_id": "TRANSACTION_ID", "timestamp": "TIMESTAMP"}
url = "https://api.development.devicecheck.apple.com/v1/validate_device_token"
response = requests.post(url, headers=headers, json=data)

# Print the response
print(response.json())
```

请注意，这只是一个基本的示例。在实际应用中，您可能需要在验证设备标识符时考虑额外的事情，例如处理网络错误，存储和查找设备标识符，处理设备标识符变化的情况等。


#### You:
上面示例代码中 YOUR_PRIVATE_KEY_ID、YOUR_TEAM_ID 和 YOUR_PRIVATE_KEY 都是怎样来的？

#### ChatGPT:
在使用DeviceCheck API时，Apple要求您使用JSON Web Token (JWT)来验证请求。为了创建这个JWT，您需要以下几个信息：

1. **YOUR\_PRIVATE\_KEY\_ID：** 这是您在Apple开发者网站生成的App的特定的Key ID。

2. **YOUR\_TEAM\_ID：** 这是您在Apple开发者帐号里的Team ID。

3. **YOUR\_PRIVATE\_KEY：** 这是与YOUR\_PRIVATE\_KEY\_ID对应的私钥。

以下是获取这些信息的步骤：

**获取 YOUR\_PRIVATE\_KEY\_ID 和 YOUR\_PRIVATE\_KEY：**

1. 访问[Apple开发者网站](https://developer.apple.com/account/)，并登入您的开发者账户。
2. 在左侧导航栏中，点击"Certificates, Identifiers & Profiles"。
3. 在弹出的页面中，点击左侧的"Keys"。
4. 点击右上角的"+"按钮来创建一个新的key。
5. 输入Key的名称，并且在Key服务列表中选择"DeviceCheck"，然后点击"Continue"。
6. 在确认页点击"Register"，然后在下一页点击"Download"下载私钥(.p8文件)。
7. 最后，你会看到一个Key ID，这就是YOUR\_PRIVATE\_KEY\_ID。
8. 下载的.p8文件包含YOUR\_PRIVATE\_KEY。你需要用一个文本编辑器打开它，然后把里面的内容复制出来。

**获取 YOUR\_TEAM\_ID：**

1. 访问[Apple开发者网站](https://developer.apple.com/account/)，并登入您的开发者账户。
2. 在左侧导航栏中，点击"Membership"。
3. 在页面中，你会看到"Team ID"，这就是YOUR\_TEAM\_ID。

完成以上步骤后，您应该已经获取到了YOUR\_PRIVATE\_KEY\_ID，YOUR\_TEAM\_ID和YOUR\_PRIVATE\_KEY，然后就可以把它们填入到上面的Python代码中，然后通过苹果的DeviceCheck API验证设备标识符了。


#### You:
请给我一份具体请求和响应的示例数据

#### ChatGPT:
请求和响应的示例数据取决于您使用的具体设备标识符和交易ID。以下是一个基本的例子，设备标识符和交易ID已经被预先填充。

**请求**

假设您有如下的设备标识符和交易ID：

- 设备标识符 (DEVICE\_TOKEN) : "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0e1f2"
- 交易ID (TRANSACTION\_ID) : "transaction\_1234"
- 时间戳(TIMESTAMP): 1597350781 (Unix时间戳格式)

那么，您的请求体将是：

```json
{
  "device_token": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0e1f2",
  "transaction_id": "transaction_1234",
  "timestamp": 1597350781
}
```

**响应**

以下是一个可能的成功响应示例：

```json
{
  "status": 0,
  "bit0": true,
  "bit1": false,
  "bit2": false,
  "bit3": false,
  "last_update_time": 1597350782
}
```

在这个响应中：

- "status"是一个数字，表示请求的结果。0表示成功，1表示错误。
- "bit0"，"bit1"，"bit2"和"bit3"是布尔值，表示设备标识符的状态。您可以在服务器上设置这些位来表示特定的设备行为或状态。
- "last\_update\_time"是一个Unix时间戳，表示设备标识符的最后更新时间。

请注意，这些都是示例值。在实际应用中，设备标识符和交易ID会有所不同，并且响应可能会根据实际情况而变化。


#### You:
App Attest API 和 DeviceCheck有什么关联和区别？App Attest API  该怎样使用，描述具体的执行逻辑，并给我 具体的实现代码

#### ChatGPT:
Apple的App Attest API和DeviceCheck API都是用于在iOS设备上增加安全性和防止欺诈行为的工具，但是它们的使用场景和目标是有所不同的。

**DeviceCheck API**主要用于在服务器和苹果设备之间生成和共享一个唯一的设备标识符，开发者可以使用这个标识符在不泄露用户隐私的情况下追踪设备的行为。例如，如果你的应用有一个免费试用期，你可以使用DeviceCheck来确定一个设备是否已经利用过这个试用期，防止用户通过多次安装应用来重复使用试用期。

**App Attest API**则是用于在服务器和客户端之间建立一个安全的通道，防止对服务器的欺诈和恶意攻击。App Attest可以生成一个设备特定的、在苹果设备上保护的密钥，并且可以用这个密钥来签名服务器请求。服务器可以验证这个签名来确定请求是否来自合法的客户端。

以下是使用App Attest API的一般步骤：

1. 在您的iOS应用中，使用`DCAppAttestService.shared.attestKey(_:completionHandler:)`方法生成一个新的密钥对，这个密钥对会被存储在设备的安全区域中。

2. 使用`DCAppAttestService.shared.generateAssertion(_:clientDataHash:completionHandler:)`方法生成一个用于服务器验证的断言。

3. 把断言和其他相关数据（例如，用户ID或设备ID）发送到服务器。

4. 在服务器上，使用Apple的App Attest服务验证断言。

5. 如果断言验证成功，服务器可以认为客户端是一个合法的、没有被篡改的应用。

以下是一些使用App Attest API的示例代码：

```swift
import DeviceCheck

let keyId = "com.example.app.attestkey"
let clientData = "Example Client Data".data(using: .utf8)!

// Generate the key
DCAppAttestService.shared.attestKey(keyId, completionHandler: { (attestationData, error) in
    if let data = attestationData {
        // Send the attestationData to the server
    } else if let error = error {
        // Handle the error
    }
})

// Generate the assertion
DCAppAttestService.shared.generateAssertion(keyId, clientDataHash: clientData, completionHandler: { (assertion, error) in
    if let assertion = assertion {
        // Send the assertion to the server
    } else if let error = error {
        // Handle the error
    }
})
```

请注意，这只是一个基本的示例，实际使用时可能需要根据您的应用和服务器的具体情况进行一些调整。


#### You:
上面关于 App Attest API 的示例代码只有客户端的，在拿到对应的attestationData 和 assertion 后还应该怎样处理呢？怎样查询服务端以及验证？

#### ChatGPT:
在生成attestationData和assertion后，你需要将其发送到你的应用后端服务器，然后使用App Attest API服务进行验证。

以下是详细步骤：

1. **发送至服务器**

```swift
if let data = attestationData {
    // Convert the data to base64
    let attestationString = data.base64EncodedString()

    // Create a request
    var request = URLRequest(url: URL(string: "https://your-server.com/attest")!)
    request.httpMethod = "POST"
    request.httpBody = attestationString.data(using: .utf8)
    
    // Send the request
    URLSession.shared.dataTask(with: request) { (data, response, error) in
        if let error = error {
            // Handle the error
        } else if let data = data {
            // Handle the response
        }
    }.resume()
}
```

2. **服务器验证**

在你的后端服务器上，你需要验证收到的attestationData和assertion。首先，你需要使用Base64解码attestationData和assertion，然后使用Apple的App Attest服务进行验证。以下是一个使用Python实现的基本示例：

```python
import requests
import jwt

# The attestationData and assertion received from the client
attestation_data = "..."
assertion = "..."

# Create the JWT
header = {"alg": "ES256", "kid": "YOUR_PRIVATE_KEY_ID"}
payload = {"iss": "YOUR_TEAM_ID", "iat": "YOUR_TIMESTAMP"}
private_key = "YOUR_PRIVATE_KEY"
token = jwt.encode(payload, private_key, algorithm='ES256', headers=header)

# Send the request to validate the attestation
headers = {"Authorization": f"Bearer {token}"}
data = {"attestationObject": attestation_data}
url = "https://api.development.appattest.apple.com/v1/attestAttestation"
response = requests.post(url, headers=headers, json=data)

# If the attestation is valid, validate the assertion
if response.status_code == 200:
    data = {"assertion": assertion}
    url = "https://api.development.appattest.apple.com/v1/attestAssertion"
    response = requests.post(url, headers=headers, json=data)

# Print the response
print(response.json())
```

在这个示例中，服务器首先验证了来自客户端的attestationData，如果它是有效的，服务器将继续验证assertion。如果两者都是有效的，那么客户端可以被视为是一个合法的、未被篡改的应用。如果有任何验证失败，服务器将返回一个错误。

请注意，这只是一个基本的示例，实际使用时可能需要根据你的应用和服务器的具体情况进行一些调整。例如，你可能需要将验证结果存储在数据库中，或者添加一些额外的错误处理逻辑。





