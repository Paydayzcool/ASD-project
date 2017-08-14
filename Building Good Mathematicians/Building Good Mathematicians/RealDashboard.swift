//
//  RealDashboard.swift
//  Building Good Mathematicians
//
//  Created by Eu Guan Koh on 14/8/17.
//  Copyright © 2017 sqrt(i). All rights reserved.
//

import UIKit

class RealDashboard: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    @IBOutlet weak var options: UITableView!
    let rows = ["Overview","Homework","Revision","Assignments","Settings"]
    override func viewDidLoad() {
        super.viewDidLoad()
        options.delegate = self
        options.dataSource = self
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */
    
    // MARK: - Table view data source
    
    func numberOfSections(in tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return rows.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "reuseIdentifier", for: indexPath)
        
        // Configure the cell...
        cell.textLabel!.text = rows[indexPath.row]
        
        return cell
    }
    
    /*func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
    }*/

}
