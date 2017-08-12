//
//  ViewController.swift
//  Building Good Mathematicians
//
//  Created by Eu Guan Koh on 6/8/17.
//  Copyright © 2017 sqrt(i). All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var usernameTextField: UITextField!

    @IBOutlet weak var passwordTextField: UITextField!
    
    @IBAction func BTNLogin(_ sender: Any) {
        performSegue(withIdentifier: "LoggingIn", sender: self)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

