using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class upDownScript : MonoBehaviour
{
    public PlayerScript ps;
    float speed;
    float fstPozY;

    // Start is called before the first frame update
    void Start()
    {
        ps = GameObject.Find("Player").GetComponent<PlayerScript>();
        fstPozY = transform.position.y;
    }

    // Update is called once per frame
    void Update()
    {
        //  スピード変更
        if(speed >= 0) speed = 0.005f * ps.life;
        if(speed < 0) speed = -0.005f * ps.life;

        //  上下往復
        float nowPozY = transform.position.y;
        if(nowPozY < fstPozY - 2f){
            speed *= -1f;
        }
        if(nowPozY > fstPozY + 2f){
            speed *= -1f;
        }
        
        transform.Translate(0f, speed, 0f);
        
    }
}
