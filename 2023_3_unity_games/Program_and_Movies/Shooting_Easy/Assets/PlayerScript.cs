using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerScript : MonoBehaviour
{
    float speed = 0.1f;
    public Rigidbody rb;
    public GameObject playerShoot;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //  弾を出す
        if(Input.GetKeyDown(KeyCode.Space)){
            Vector3 pos = transform.position + transform.up * 1.5f;
            GameObject shootClone = Instantiate(playerShoot, pos, transform.rotation);
            Rigidbody shootrb = shootClone.GetComponent<Rigidbody>();
        }

        //  左右の移動
        float directiron = Input.GetAxisRaw("Horizontal");
        if(-8 < transform.position.x && transform.position.x < 8){
            transform.Translate(directiron * speed, 0f, 0f);
        }

    }
}
