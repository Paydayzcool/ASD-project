//
//  ViewController.swift
//  LearningTableViews
//
//  Created by Callum Koh on 22/8/17.
//  Copyright © 2017 pop("Goes the weasel"). All rights reserved.
//

import UIKit
import Foundation

class ViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    private var data: [String] = []

    @IBOutlet weak var tableView: UITableView!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        for i in 0...1000 {
            data.append("\(i)")
        }
        tableView.dataSource = self
        
    }


    
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return data.count
    }
    
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cellReuseIdentifier") as! CustomTableViewCell //1.
        
        let text = data[indexPath.row] //2.
        
        cell.label .text = text //3.
        
        return cell //4.
    }

}

