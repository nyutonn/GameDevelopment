using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TargetController : MonoBehaviour
{
    public int targetCount;
    public void FixedUpdate()
    {
        targetCount = transform.childCount - 2;
    }
}