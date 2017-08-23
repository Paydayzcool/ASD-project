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
    var data: [String] = ["1","2","3","4"]
    var extras: [String] = ["A","B","C","D"]

    @IBOutlet weak var tableView: UITableView!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        // Getting this class to comform to the UITableView delegate and data source classes. If you right click either UITableViewDataSource or UITableViewDelegate and click "Jump to definition", you will notice the compulsory and optional functions available to you. BRILLIANT!
        tableView.delegate = self
        tableView.dataSource = self
        
    }


    
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return data.count
    }
    
    // This creates the cells and colours them. Pretty self explanatory.
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        // Ensures that the program is writing cells into the correct tableView, especially useful when there are more than one tableViews on the same viewControllers.
        let cell = tableView.dequeueReusableCell(withIdentifier: "cellReuseIdentifier") as! CustomTableViewCell
        
        // Getting the tbleView cell titles from the array named "data"
        let text = data[indexPath.row]
        
        // NOTE: this line says "label" and not "textLabel?" because in CustomTableViewCell.swift, the tableViewCell replaces this. If you try getting xCode to autoComplete your code, you will notice that the cell label text has type "tableView" from CustomTableViewCell.swift
        cell.label.text = text
        
        if indexPath.row % 2 == 0 {
            cell.contentView.backgroundColor = UIColor.red
        } else {
            cell.contentView.backgroundColor = UIColor.lightGray
        }
        
        return cell
    }
    
    // This just checks whether the user has selected the row. Or whatever...
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
        // This line stops the table cell from appearing as selected.
        tableView.deselectRow(at: indexPath, animated: true)
        
        /*
         This code just allows alerts, uncomment this if you want, but I don't think you'll get anywhere with this.
         let alertController = UIAlertController(title: "Hint",message: "You have selected row \(indexPath.row)",preferredStyle: .alert)
        let alertAction = UIAlertAction(title: "OK", style: .cancel, handler: nil)
        
        alertController.addAction(alertAction)
        
        present(alertController, animated:true, completion:nil)*/
        
        
        // Getting into the viewController names - check the storyboard and select the added viewControllers. If you check the details in the third icon, you'll find that the storyboard IDs are the same as the ones in extras.
        let vcName = extras[indexPath.row]
        
        // This creates the segues or links between the tableView and the viewControllers.
        let viewController = storyboard?.instantiateViewController(withIdentifier: vcName)
        
        // This initiates the viewController links.
        self.navigationController?.pushViewController(viewController!, animated: true)
        
    }

}

