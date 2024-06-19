using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class wallScript : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.Translate(0.03f, 0f, 0f);
        if(transform.position.x > 13f){
            transform.position = new Vector3(-1f, 0f, 1.0f);
        }
    }
}
