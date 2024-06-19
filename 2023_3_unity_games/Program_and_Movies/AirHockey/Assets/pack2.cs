using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class pack2 : MonoBehaviour
{
    Vector3 pos;
    Rigidbody rb;
    public Text score_text;
    int red_score = 0;
    int blue_score = 0;
    
    
    // Start is called before the first frame update
    void Start()
    {
        transform.position = new Vector3(0f, -9f, -10f);
        pos = transform.position;
        score_text.text = red_score + "-" + blue_score;
    }

    // Update is called once per frame
    void Update()
    {
        
        // Debug.Log(red_score +"-"+ blue_score);
    }
    void OnCollisionEnter(Collision collision)
    {
        rb = this.GetComponent<Rigidbody>();
        if (collision.gameObject.tag == "Red")
        {  
            red_score += 1;
            score_text.text = red_score + "-" + blue_score;
            transform.position = pos;
            rb.velocity = new Vector3(0, 0, 0);
        }
        if(collision.gameObject.tag == "Blue")
        {
            blue_score += 1;
            score_text.text = red_score + "-" + blue_score;
            transform.position = pos;
            rb.velocity = new Vector3(0, 0, 0);

        }
        

    }
}
