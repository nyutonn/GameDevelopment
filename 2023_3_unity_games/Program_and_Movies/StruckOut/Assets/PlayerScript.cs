using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerScript : MonoBehaviour
{
    public GameObject bullet;
    float power = 0f;
    int count = 10;
    public Text countText;

    float speed = 0.01f;
    public Slider slider;

    public TargetController targetController;
    public Text gameOverText;
    // Start is called before the first frame update
    void Start()
    {
        gameOverText.text = "";
    }

    // Update is called once per frame
    void Update()
    {
        float direction_h = Input.GetAxisRaw("Horizontal");
        float direction_v = Input.GetAxisRaw("Vertical");
        transform.Translate(direction_h * speed, direction_v * speed, 0);

        countText.text = "残り : " + count;

        //  Spaceを離したら発射
        if(Input.GetKeyUp(KeyCode.Space) && count > 0){
            GameObject obj = Instantiate(bullet, transform.position, transform.rotation);
            Rigidbody rb = obj.GetComponent<Rigidbody>();
            rb.AddForce(obj.transform.forward * power * 1000, ForceMode.Force);
            count -= 1;
            power = 0f;
        }

        //  Spaceを押している最中に力を貯める
        if(Input.GetKey(KeyCode.Space)){
            power += 0.01f;
            slider.value = power;
            if(power > 1f) power = 0f;
        }
        //  ゲーム終了のテキスト表示
        if(targetController.targetCount == 0){
            gameOverText.text = "Game Clear!\n残り弾数：" + count;
        }
        if(count == 0){
            gameOverText.text = "GameOver\n残りの的の数：" + targetController.targetCount;
        }
    }
}
