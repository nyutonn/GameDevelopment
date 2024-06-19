using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player2 : MonoBehaviour
{
    Vector3 pos;
    Rigidbody rb;
    float moveX;
    float moveZ;
    public GameObject pack;
    // Start is called before the first frame update
    void Start()
    {

        pos = transform.position;
        
    }

    // Update is called once per frame
    void Update()
    {     

    }

    void OnMouseDrag()
    {
        float positionX = transform.position.x;
        float positionZ = transform.position.z;
        moveX = Input.GetAxis("Mouse X");
        moveZ = Input.GetAxis("Mouse Y");
        // if (positionX < 0 ||moveX <0)
        {
            // if (positionX > -9 || moveX > 0)
            {
                pos.x += 1.4f * moveX;
            }
        }
        if (positionZ < 4 || moveZ < 0)
        {
            if (positionZ > -14 || moveZ > -2)
            {
                pos.z += 1.4f * moveZ;
            }
        }
       
        transform.position = pos;  // ここがおかしい？？
        Debug.Log("x:" + moveX + "  y:" + moveZ);

        // transform.Translate(pox, 0f, moveZ);

    }
    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name == "pack")
        {
            float power = 0.01f;
            rb = pack.GetComponent<Rigidbody>();
            rb.AddForce(new Vector3(moveX * power, 0f, moveZ * power), ForceMode.Impulse);
        }
       
    }
}
