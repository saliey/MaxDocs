



# 总结

objc_msgSend

resolveInstanceMethod

resolveClassMethod

forwardingTargetForSelector

methodSignatureForSelector

forwardInvocation

NSInvocation








# iOS反射机制及应用

#### You:
给我 讲述下 iOS 的反射机制，相关函数有哪些？反射的原理是什么？反射能够做哪些事情？

#### ChatGPT:
在 iOS 中，反射（Reflection）机制主要是通过 Objective-C 的运行时系统（Runtime）来实现的。运行时系统是 Objective-C 的一种动态特性，它使得开发者可以在运行时获取类的信息，创建对象，调用方法等。

1. 反射相关的函数
   主要包括以下函数：

   - `class_getName(Class cls)`: 获取类名
   - `class_getInstanceMethod(Class cls, SEL name)`: 获取实例方法
   - `class_getClassMethod(Class cls, SEL name)`: 获取类方法
   - `class_copyMethodList(Class cls, unsigned int *outCount)`: 获取方法列表
   - `class_getInstanceVariable(Class cls, const char *name)`: 获取实例变量
   - `class_copyIvarList(Class cls, unsigned int *outCount)`: 获取所有实例变量列表
   - `class_getProperty(Class cls, const char *name)`: 获取属性
   - `class_copyPropertyList(Class cls, unsigned int *outCount)`: 获取所有属性列表
   - `objc_getClass(const char *name)`: 获取类
   - `objc_getProtocol(const char *name)`: 获取协议

2. 反射的原理
   在 Objective-C 中，每个类和对象的定义、属性、方法等信息在编译时都会被编译器收集起来，然后在程序运行时加载到内存中。运行时系统就是管理和维护这些信息的系统。通过运行时系统，开发者可以在程序运行时动态地获取到这些信息，这就是反射的原理。

3. 反射能够做的事情
   - 动态创建对象和调用方法：例如，可以根据用户的输入动态地创建对象，然后调用对象的方法。
   - 动态获取和修改对象的属性和变量：例如，可以遍历一个对象的所有属性，然后动态地修改属性的值。
   - 动态添加和替换方法：例如，可以动态地给一个类添加新的方法，或者替换掉已有的方法。
   - 动态获取类的信息：例如，可以获取一个类的所有属性和方法。

这些特性使得 Objective-C 具有很强的动态性，可以在运行时做很多编译时无法做到的事情。但同时，也要注意，过度使用反射可能会导致代码的可读性和可维护性降低，因此在实际开发中需要谨慎使用。


#### You:
xcode 怎样查看 iOS framework 所有的头文件？需要了解 framework 的知识，我需要怎样的学习方法

#### ChatGPT:
在 Xcode 中，你可以通过以下步骤查看 iOS framework 的所有头文件：

1. 在 Xcode 的左侧导航栏中，找到你的项目。
2. 在项目下找到你想要查看的 framework（它通常位于你项目的 "Frameworks" 文件夹下）。
3. 右键点击这个 framework，然后选择 "Show in Finder"。
4. 在 Finder 中找到这个 framework，然后右键点击它，选择 "Show Package Contents"。
5. 在打开的文件夹中，你可以找到 "Headers" 文件夹，这个文件夹下就是 framework 的所有头文件。

关于 framework 的学习，你可以按照以下步骤进行：

1. **理解什么是 Framework**：Framework 在 iOS 开发中是一个重要的组件，它是用来封装一组功能，并可以供其他应用程序调用的代码库。它包含了代码（可能是 Swift，Objective-C 或者其他语言编写的），也可能包含了资源文件（如图片，音频，xib，storyboard 等）。

2. **学习如何创建和使用 Framework**：你可以找一些教程或者官方的文档，学习如何在 Xcode 中创建一个新的 framework，然后在其他项目中如何使用这个 framework。

3. **学习 Framework 的版本管理和分发**：如果你想要创建一个可以被其他人使用的 framework，你还需要学习如何进行版本管理（例如如何使用 git 和 GitHub），以及如何分发你的 framework（例如通过 CocoaPods 或者 Carthage）。

4. **阅读开源 Framework 的源代码**：如果你想要更深入地理解 framework，阅读一些开源的 framework 的源代码是一个很好的方法。通过阅读源代码，你可以理解它们是如何设计和实现的，以及如何解决实际问题的。

5. **编写和测试自己的 Framework**：通过自己动手实践，你可以更深入地理解 Framework。尝试编写一个简单的 Framework，并尝试在其他项目中使用它，通过这个过程，你可以发现并解决一些实际的问题。

以上就是对于 iOS Framework 的学习建议，希望对你有所帮助。


#### You:
给我讲述下 iOS runtime  的原理。以及穷举所涉及到的术语，比如 isa/imp/sel 等，并介绍这些模块或结构体的作用

#### ChatGPT:
Objective-C 的运行时（runtime）系统是一套动态类型语言的基础设施，你可以在程序运行时（而不仅仅是在编译时）添加类，检查并修改类和对象，以及向它们发送消息。

以下是一些与 Objective-C 运行时系统相关的关键概念和术语：

1. **isa**：每个 Objective-C 对象都有一个名为 `isa` 的指针，指向该对象所属的类，也就是说 `isa` 确定了对象是什么类的实例。这是对象和它的类之间建立关系的关键。

2. **Class**：类在 Objective-C 中也是一个对象，每个类都有一个 `Class` 结构体。这个结构体包含了类的元数据，比如父类，实例变量的大小，类的名称，以及一个指向方法列表的指针等。

3. **SEL**：`SEL` 是 "selector" 的简写，是一个在运行时被注册的方法/函数名。当你向一个对象发送一个消息，实际上是在传递一个 selector。Selector 通过 `@selector()` 方法在编译时确定，或者通过 `NSSelectorFromString()` 在运行时确定。

4. **IMP**：`IMP` 是 "implementation" 的简写，它是指向 Objective-C 方法实现的指针，这个方法实现是一个函数，接受至少两个参数——接收者和 selector。

5. **Method**：方法是由一个 selector 和一个 IMP 构成的。在类的方法列表中，每个方法都以这种形式存在。

6. **消息传递**：在 Objective-C 中，你不直接调用方法，而是通过发送消息的方式来调用。当你发送一个消息给一个对象，运行时系统会通过对象的 `isa` 指针找到对象所属的类，然后在类的方法列表中寻找和 selector 匹配的方法，找到后通过调用方法的 IMP 来执行方法。

这些就是 Objective-C 运行时系统的一些核心概念和术语，它们共同构成了 Objective-C 的动态特性的基础。通过理解这些概念和术语，你可以更深入地理解 Objective-C 的运行时机制。


#### You:
方法调用在 runtime 内的具体执行逻辑是什么？我是初学者，请详细的给我讲述，我需要了解整体的底层逻辑

#### ChatGPT:
Objective-C 的方法调用实际上是通过运行时（runtime）系统来进行的消息传递。当你在代码中调用一个方法，例如 `[object doSomething]`，实际上发生的是你向 `object` 对象发送了一个 `doSomething` 的消息。这种消息传递的过程如下：

1. **开始消息发送**：当你向一个对象发送一个消息时，实际上会调用 `objc_msgSend` 函数，这个函数的两个主要参数分别是消息的接收者（`object`）和消息（`doSomething` 的 selector）。

2. **查找接收者的类**：`objc_msgSend` 函数会通过接收者的 `isa` 指针找到接收者所属的类。

3. **在方法列表中查找方法**：然后，`objc_msgSend` 会在这个类的方法列表中查找和 selector 匹配的方法。如果找到，就跳到第5步。如果没找到，就进入第4步。

4. **查找父类的方法列表**：如果在类的方法列表中没有找到和 selector 匹配的方法，`objc_msgSend` 会继续在类的父类的方法列表中查找，一直到根类（通常是 `NSObject`）。如果在整个继承链上都没有找到和 selector 匹配的方法，就会进入动态方法解析和消息转发的流程。

5. **调用方法的实现**：一旦在某个类的方法列表中找到了和 selector 匹配的方法，`objc_msgSend` 就会通过调用方法的 `IMP` （实现）来执行方法。`IMP` 是一个函数指针，这个函数的第一个参数是方法的接收者，第二个参数是 selector，后面的参数是你在调用方法时传入的参数。

以上就是 Objective-C 方法调用（或者说消息发送）的基本流程。这个流程包含了一些 Objective-C 的核心特性，比如动态方法查找，动态方法解析，消息转发等。通过理解这个流程，你可以更深入地理解 Objective-C 的动态特性和运行时系统。


#### You:
如果在整个继承链上都没有找到和 selector 匹配的方法，就会进入动态方法解析和消息转发的流程。 这里说的动态方法解析和消息转发是指什么？逻辑是什么？

#### ChatGPT:
如果在整个继承链上都没有找到匹配的方法（也就是没有找到与 selector 对应的 `IMP`），那么 Objective-C 的运行时系统会提供几种机制来处理这种情况，它们依次是：动态方法解析、快速转发（Fast Forwarding）、标准消息转发（Normal Forwarding）和最后的未找到方法处理。

1. **动态方法解析**：Objective-C 允许你动态地提供一个方法的实现。当运行时系统找不到一个方法的实现时，它会调用对象的 `+resolveInstanceMethod:`（对实例方法）或 `+resolveClassMethod:`（对类方法）方法，这个方法的参数就是那个未找到的 selector。在这个方法中，你可以动态地提供一个方法的实现。如果你提供了，那么运行时系统就会重新启动方法查找过程，如果没有提供，那么运行时系统就会进入下一步：快速转发。

2. **快速转发**：运行时系统会调用对象的 `-forwardingTargetForSelector:` 方法，这个方法的参数就是那个未找到的 selector。在这个方法中，你可以返回一个可以响应这个 selector 的其他对象。如果你返回了这样的对象，那么运行时系统就会向这个对象重新发送这个消息。如果你返回 `nil` 或者不实现这个方法，那么运行时系统就会进入下一步：标准消息转发。

3. **标准消息转发**：这是一种更复杂、更灵活的消息转发机制。运行时系统会先调用对象的 `-methodSignatureForSelector:` 方法来获取未找到的方法的参数和返回值类型，如果这个方法返回了一个有效的方法签名，那么运行时系统就会创建一个 `NSInvocation` 对象，然后调用对象的 `-forwardInvocation:` 方法，这个方法的参数就是刚刚创建的 `NSInvocation` 对象。在 `-forwardInvocation:` 方法中，你可以自由地修改 `NSInvocation` 对象，然后将消息转发给其他对象。如果 `-methodSignatureForSelector:` 返回 `nil` 或者你没有实现 `-forwardInvocation:` 方法，那么运行时系统就会进入下一步：未找到方法处理。

4. **未找到方法处理**：最后，运行时系统会调用对象的 `-doesNotRecognizeSelector:` 方法，这个方法的参数就是那个未找到的 selector。默认的实现会引发一个异常，你可以覆盖这个方法来提供自己的处理方式，比如打印一条错误信息。

以上就是当 Objective-C 的运行时系统在整个继承链上都没有找到一个方法的实现时的处理流程。通过这个流程，Objective-C 提供了非常强大的动态特性和灵活性。


#### You:
关于上面两步讲的消息传递、动态方法解析、消息转发所对应的每一步，请给我举一个具体的示例。注意是每一步都要有对应的代码示例，以便于我能理解具体的逻辑。注意给出的代码尽量简明，代码要有对应的文件名，以及变量名要能够上下文匹配。

#### ChatGPT:
好的，下面我将使用 Objective-C 的示例代码来解释上述的每一个步骤。假设我们有一个 `MyClass` 类，我们将会通过它来演示。

首先是消息传递的代码：

```Objective-C
// 文件名：MyClass.m

@implementation MyClass

- (void)myMethod {
    NSLog(@"MyMethod is called!");
}

@end
```

在这个类中，我们有一个方法叫做 `myMethod`。当我们想要调用这个方法时，我们可以通过下面的代码：

```Objective-C
// 文件名：main.m

MyClass *myObject = [[MyClass alloc] init];
[myObject myMethod];  // 这是一个消息发送
```

接下来是动态方法解析的代码：

```Objective-C
// 文件名：MyClass.m

void dynamicMethodIMP(id self, SEL _cmd) {
    NSLog(@"Dynamic method is called!");
}

@implementation MyClass

+ (BOOL)resolveInstanceMethod:(SEL)sel {
    if (sel == @selector(dynamicMethod)) {
        class_addMethod([self class], sel, (IMP)dynamicMethodIMP, "v@:");
        return YES;
    }
    return [super resolveInstanceMethod:sel];
}

@end
```

在这个例子中，如果我们尝试调用一个名为 `dynamicMethod` 的方法，那么 `+resolveInstanceMethod:` 就会被调用，然后我们就会动态地添加一个方法。

最后是消息转发的代码：

```Objective-C
// 文件名：MyClass.m

@implementation MyClass

- (id)forwardingTargetForSelector:(SEL)aSelector {
    if (aSelector == @selector(forwardedMethod)) {
        return someOtherObject;  // someOtherObject 是可以响应 forwardedMethod 方法的其他对象
    }
    return [super forwardingTargetForSelector:aSelector];
}

@end
```

在这个例子中，如果我们尝试调用一个名为 `forwardedMethod` 的方法，那么 `-forwardingTargetForSelector:` 就会被调用，然后我们就会把这个消息转发给 `someOtherObject`。

这些都是 Objective-C 的动态特性和灵活性的例子。通过理解这些例子，你可以更深入地理解 Objective-C 的运行时系统。


#### You:
你上面的这个示例看的我一头雾水，从 """[myObject myMethod];""" 方法后我就看不懂了，谁调用谁，谁触发了谁，不要节省步骤，要尽量详细，因为我是初学者。请重新输出

#### ChatGPT:
对不起，我了解你的困惑，让我们详细解析每个步骤。我们仍然使用上述的 `MyClass` 类来进行说明。

首先，假设我们有如下的 MyClass 类定义：

```Objective-C
// 文件名：MyClass.m

#import "MyClass.h"

@implementation MyClass

- (void)myMethod {
    NSLog(@"myMethod is called!");
}

@end
```

`MyClass` 类有一个实例方法叫做 `myMethod`。现在我们创建一个 `MyClass` 的实例，并调用 `myMethod` 方法：

```Objective-C
// 文件名：main.m

#import "MyClass.h"

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        MyClass *myObject = [[MyClass alloc] init];
        [myObject myMethod];
    }
    return 0;
}
```

在这个例子中，当 `myMethod` 方法被调用时，就相当于我们向 `myObject` 对象发送了一个 `myMethod` 的消息。在运行时系统中，这个调用会被转化为 `objc_msgSend(myObject, @selector(myMethod))`。

然后，假设我们尝试调用一个 `MyClass` 类中不存在的方法 `nonExistentMethod`：

```Objective-C
// 文件名：main.m

#import "MyClass.h"

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        MyClass *myObject = [[MyClass alloc] init];
        [myObject nonExistentMethod];  // 该方法在 MyClass 中并不存在
    }
    return 0;
}
```

由于 `MyClass` 中并不存在 `nonExistentMethod`，在尝试调用此方法时，Objective-C 运行时会启动消息转发流程。首先，Objective-C 运行时会尝试进行动态方法解析。下面的代码是 `MyClass` 进行动态方法解析的一个例子：

```Objective-C
// 文件名：MyClass.m

#import "MyClass.h"
#import <objc/runtime.h>

void dynamicMethodIMP(id self, SEL _cmd) {
    NSLog(@"dynamicMethodIMP is called!");
}

@implementation MyClass

+ (BOOL)resolveInstanceMethod:(SEL)sel {
    if (sel == @selector(nonExistentMethod)) {
        class_addMethod([self class], sel, (IMP)dynamicMethodIMP, "v@:");
        return YES;
    }
    return [super resolveInstanceMethod:sel];
}

@end
```

在这个例子中，当 `nonExistentMethod` 方法被调用时，`+resolveInstanceMethod:` 方法会被触发。因为 `nonExistentMethod` 在 `MyClass` 中不存在，我们在 `+resolveInstanceMethod:` 中为其动态添加一个实现 `dynamicMethodIMP`。如果成功添加，我们返回 YES 表示方法已经被成功解析，然后 `dynamicMethodIMP` 就会被调用。

然后，如果动态方法解析失败（`+resolveInstanceMethod:` 返回了 NO），Objective-C 运行时会尝试进行消息转发。首先会尝试进行快速转发，即调用 `-forwardingTargetForSelector:` 方法：

```Objective-C
// 文件名：MyClass.m

#import "MyClass.h"
#import "AnotherClass.h"  // 假设 AnotherClass 是另一个类，实现了 nonExistentMethod

@implementation MyClass

- (id)forwardingTargetForSelector:(SEL)aSelector {
    if (aSelector == @selector(nonExistentMethod)) {
        return [AnotherClass new];
    }
    return [super forwardingTargetForSelector:aSelector];
}

@end
```

在这个例子中，当 `nonExistentMethod` 方法被调用时，`-forwardingTargetForSelector:` 方法会被触发。我们在这个方法中返回了一个 `AnotherClass` 的新实例，该实例能够响应 `nonExistentMethod` 方法。因此，`nonExistentMethod` 的消息会被转发给这个 `AnotherClass` 的实例。

以上就是 Objective-C 的消息发送、动态方法解析和消息转发的示例。这些特性使 Objective-C 具有强大的动态性和灵活性。希望这个更详细的解释能帮助你理解这些概念。
