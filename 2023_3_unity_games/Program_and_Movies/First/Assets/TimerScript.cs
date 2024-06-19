using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TimerScript : MonoBehaviour
{
    float timer = 0f;
    float timer2 = 0f;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        timer += Time.deltaTime;
        timer2 += 0.01f;
        // Debug.Log(timer + ":deltaTime, " + timer2);
    }
}
