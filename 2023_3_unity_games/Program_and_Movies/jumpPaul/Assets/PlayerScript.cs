using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerScript : MonoBehaviour
{
    public Rigidbody rb;
    public float power = 5f;
    bool jumpFlag = false;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.Space) && !jumpFlag){
            rb.AddForce(transform.up * power, ForceMode.Impulse);
            jumpFlag = true;
        }   
    }

    void OnCollisionEnter(Collision collision){
        if(collision.gameObject.name == "floor"){
            jumpFlag = false;
        }
    }
}
