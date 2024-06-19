using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class leftScript : MonoBehaviour
{
    // here!!
    // 他のスクリプトから変数を持ってくる
    public PlayerScript ps;
    float speed;

    // Start is called before the first frame update
    void Start()
    {
        // ps = GameObject.Find("Player").GetComponent<PlayerScript>();
    }

    // Update is called once per frame
    void Update()
    {
        // here!!
        // 他のスクリプトから変数を持ってくる
        speed = -0.02f * ps.life;
        transform.Translate(speed, 0f, 0f);
    }
}
