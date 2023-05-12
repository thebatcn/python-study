好的，以下是一个简单的文字游戏，使用class创建场景的代码示例：

```javascript
class Scene {
  constructor(description, options) {
    this.description = description;
    this.options = options;
  }
  
  play() {
    console.log(this.description);
    for (let i = 0; i < this.options.length; i++) {
      console.log(`${i + 1}. ${this.options[i].text}`);
    }
    const choice = prompt("请选择一个选项：");
    if (choice > 0 && choice <= this.options.length) {
      this.options[choice - 1].action();
    } else {
      console.log("无效的选项，请重新选择。");
      this.play();
    }
  }
}

const startScene = new Scene(
  "你醒来发现自己在一个陌生的房间里，四周一片漆黑。你该怎么办？",
  [
    {
      text: "寻找出口",
      action: function() {
        console.log("你摸索着四周，终于找到了一扇门。");
        nextScene.play();
      }
    },
    {
      text: "呼救",
      action: function() {
        console.log("你大声呼救，但没有任何回应。");
        nextScene.play();
      }
    }
  ]
);

const nextScene = new Scene(
  "你打开门，发现自己置身于一片荒野之中。你该往哪个方向走？",
  [
    {
      text: "向东走",
      action: function() {
        console.log("你向东走了一段路，发现了一座城镇。");
        endScene.play();
      }
    },
    {
      text: "向南走",
      action: function() {
        console.log("你向南走了一段路，遇到了一只凶猛的野兽。");
        loseScene.play();
      }
    }
  ]
);

const endScene = new Scene(
  "你来到了城镇，终于获得了自由。恭喜你通关！",
  []
);

const loseScene = new Scene(
  "你被野兽杀死了，游戏结束。",
  []
);

startScene.play();
```

这个游戏有三个场景：起始场景、下一个场景和结束场景。每个场景都有一个描述和一些选项，玩家可以选择其中一个选项来继续游戏。每个选项都有一个文本和一个动作，动作可以是打印一些文本或者跳转到下一个场景。玩家的选择会影响游戏的进程，最终会通关或者失败。