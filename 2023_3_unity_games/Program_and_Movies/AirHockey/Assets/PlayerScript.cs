using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerScript : MonoBehaviour
{
    public Rigidbody packrb;
    float mouse_x;
    float mouse_y;
    float speed = 1f;
    float power = 0.05f;

    Vector3 add;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
    }

    void OnCollisionEnter(Collision collision){
        // if(collision.gameObject.name == "pack"){
            packrb.AddForce(add * power, ForceMode.Impulse);
        // }
    }

    void OnMouseDrag(){
        mouse_x = Input.GetAxis("Mouse X");
        mouse_y = Input.GetAxis("Mouse Y");
        transform.Translate(mouse_x * speed, 0f, mouse_y * speed);
        add = new Vector3(mouse_x, 0f, mouse_y);
        Debug.Log("Drag");
    }
}
