//
//  MenuTableViewController.swift
//  Learning Table Sections
//
//  Created by Eu Guan Koh on 27/8/17.
//  Copyright © 2017 sqrt(i). All rights reserved.
//
/* 
 NOTES:
 I feel that we can use these sections to divide dates of particular tasks or assignments.
 Otherwise, this idea of tableView sections will come in handy at some other point.
*/

import UIKit
import Foundation

class MenuTableViewController: UITableViewController {
    
    // Defining the sections
    let sections = ["Pizza","Calzone","Pasta"]
    
    // Notice how there are three inside arrays to represent the three sections?
    let items = [["BBQ Chicken", "Pepperoni", "Hawaiian"],
                 ["Saussage","Chicken Pesto", "Prawns", "Mushroom"],
                 ["Cajun Chicken Penne", "Chicken Masala", "Chicken Parmigiana"]]
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }

    // MARK: - Table view data source

    override func numberOfSections(in tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return sections.count
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return items[section].count
    }

    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "menuItem", for: indexPath)
        
        // Configure the cell...
        
        cell.textLabel?.text = items[indexPath.section][indexPath.row]
        return cell
    }
    
    // This is one of the UITableViewController functions which defines the titles of the tableView headers.
    override func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return sections[section]
    }

    /*
    // Override to support conditional editing of the table view.
    override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            // Delete the row from the data source
            tableView.deleteRows(at: [indexPath], with: .fade)
        } else if editingStyle == .insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(_ tableView: UITableView, moveRowAt fromIndexPath: IndexPath, to: IndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
