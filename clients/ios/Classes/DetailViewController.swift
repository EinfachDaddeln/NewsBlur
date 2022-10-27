//
//  DetailViewController.swift
//  NewsBlur
//
//  Created by David Sinclair on 2020-08-27.
//  Copyright © 2020 NewsBlur. All rights reserved.
//

import UIKit

/// Manages the detail column of the split view, with the feed detail and/or the story pages.
class DetailViewController: BaseViewController {
    /// Returns the shared app delegate.
    var appDelegate: NewsBlurAppDelegate {
        return NewsBlurAppDelegate.shared()
    }
    
    /// Preference keys.
    enum Key {
        /// Layout of the story titles and story pages.
        static let layout = "story_titles_position"
        
        /// Behavior of the split controller.
        static let behavior = "split_behavior"
        
        /// Position of the divider between the views when in horizontal orientation. Only used for `.top` and `.bottom` layouts.
        static let horizontalPosition = "story_titles_divider_horizontal"
        
        /// Position of the divider between the views when in vertical orientation. Only used for `.top` and `.bottom` layouts.
        static let verticalPosition = "story_titles_divider_vertical"
    }
    
    /// Preference values.
    enum LayoutValue {
        static let left = "titles_on_left"
        static let top = "titles_on_top"
        static let bottom = "titles_on_bottom"
        static let grid = "titles_in_grid"
    }
    
    /// How the feed detail and story pages are laid out.
    enum Layout {
        /// The feed detail is to the left of the story pages (and managed by the split view, not here).
        case left
        
        /// The feed detail is at the top, the story pages at the bottom.
        case top
        
        /// The story pages are at the top, the feed detail at the bottom.
        case bottom
        
        /// Using a grid view for the story titles and story pages.
        case grid
    }
    
    /// How the feed detail and story pages are laid out.
    var layout: Layout {
        get {
            switch UserDefaults.standard.string(forKey: Key.layout) {
            case LayoutValue.top:
                return .top
            case LayoutValue.bottom:
                return .bottom
            case LayoutValue.grid:
                return .grid
            default:
                return .left
            }
        }
        set {
            guard newValue != layout else {
                return
            }
            
            switch newValue {
            case .top:
                UserDefaults.standard.set(LayoutValue.top, forKey: Key.layout)
            case .bottom:
                UserDefaults.standard.set(LayoutValue.bottom, forKey: Key.layout)
            case .grid:
                UserDefaults.standard.set(LayoutValue.grid, forKey: Key.layout)
            default:
                UserDefaults.standard.set(LayoutValue.left, forKey: Key.layout)
            }
            
            updateLayout(reload: true)
        }
    }
    
    /// Whether or not the feed detail is on the left; see also the following property.
    @objc var storyTitlesOnLeft: Bool {
        return layout == .left
    }
    
    /// Whether or not the feed detail is on the top; see also the previous property.
    @objc var storyTitlesOnTop: Bool {
        return layout == .top
    }
    
    /// Whether or not using the grid layout; see also the previous property.
    @objc var storyTitlesInGrid: Bool {
        return layout == .grid
    }
    
    /// Preference values.
    enum BehaviorValue {
        static let auto = "auto"
        static let tile = "tile"
        static let displace = "displace"
        static let overlay = "overlay"
    }
    
    /// How the split controller behaves.
    enum Behavior {
        /// The split controller figures out the best behavior.
        case auto
        
        /// The split controller arranges the views side-by-side.
        case tile
        
        /// The split controller pushes the detail view aside.
        case displace
        
        /// The split controller puts the left columns over the detail view.
        case overlay
    }
    
    /// How the split controller behaves.
    var behavior: Behavior {
        switch UserDefaults.standard.string(forKey: Key.behavior) {
        case BehaviorValue.tile:
            return .tile
        case BehaviorValue.displace:
            return .displace
        case BehaviorValue.overlay:
            return .overlay
        default:
            return .auto
        }
    }
    
    /// Returns `true` if the window is in portrait orientation, otherwise `false`.
    @objc var isPortraitOrientation: Bool {
        return view.window?.windowScene?.interfaceOrientation.isPortrait ?? false
    }
    
    /// Position of the divider between the views.
    var dividerPosition: CGFloat {
        get {
            let key = isPortraitOrientation ? Key.verticalPosition : Key.horizontalPosition
            let value = CGFloat(UserDefaults.standard.float(forKey: key))
            
            if value == 0 {
                return 200
            } else {
                return value
            }
        }
        set {
            guard newValue != dividerPosition else {
                return
            }
            
            let key = isPortraitOrientation ? Key.verticalPosition : Key.horizontalPosition
            
            UserDefaults.standard.set(Float(newValue), forKey: key)
        }
    }
    
    /// Top container view.
    @IBOutlet weak var topContainerView: UIView!
    
    /// Bottom container view.
    @IBOutlet weak var bottomContainerView: UIView!
    
    /// Draggable divider view.
    @IBOutlet weak var dividerView: UIView!
    
    /// Indicator image in the divider view.
    @IBOutlet weak var dividerImageView: UIImageView!
    
    /// Top container view top constraint. May need to adjust this for fullscreen on iPhone.
    @IBOutlet weak var topContainerTopConstraint: NSLayoutConstraint!
    
    /// Bottom constraint of the divider view.
    @IBOutlet weak var dividerViewBottomConstraint: NSLayoutConstraint!
    
    /// The navigation controller managed by the split view controller, that encloses the immediate navigation controller of the detail view when in compact layout.
    @objc var parentNavigationController: UINavigationController? {
        return navigationController?.parent as? UINavigationController
    }
    
    /// The feed detail navigation controller in the supplementary pane, loaded from the storyboard.
    var supplementaryFeedDetailNavigationController: UINavigationController?
    
    /// The feed detail view controller in the supplementary pane, loaded from the storyboard.
    var supplementaryFeedDetailViewController: FeedDetailViewController?
    
    /// The feed detail view controller, if using `top`, `bottom`, or `grid` layout. `nil` if using `left` layout.
    var feedDetailViewController: FeedDetailViewController?
    
    /// Whether or not the grid layout was used the last time checking the view controllers.
    private var wasGrid = false
    
    /// The horizontal page view controller. [Not currently used; might be used for #1351 (gestures in vertical scrolling).]
//    var horizontalPageViewController: HorizontalPageViewController?
    
    /// The story pages view controller, that manages the previous, current, and next story view controllers.
    var storyPagesViewController: StoryPagesViewController? {
        return appDelegate.storyPagesViewController
    }
    
    /// Returns the currently displayed story view controller, or `nil` if none.
    @objc var currentStoryController: StoryDetailViewController? {
        return storyPagesViewController?.currentPage
    }
    
    /// Updates the layout; call this when the layout is changed in the preferences.
    @objc(updateLayoutWithReload:) func updateLayout(reload: Bool) {
        checkViewControllers()
        
        appDelegate.feedsViewController.loadOfflineFeeds(false)
        
        if layout != .left, let controller = feedDetailViewController {
            if behavior == .overlay {
                navigationItem.leftBarButtonItems = [controller.feedsBarButton, controller.settingsBarButton]
            } else {
                navigationItem.leftBarButtonItems = [controller.settingsBarButton]
            }
        } else {
            navigationItem.leftBarButtonItems = []
        }
        
        if reload {
            DispatchQueue.main.async {
                self.feedDetailViewController?.reload()
            }
        }
    }
    
    /// Update the theme.
    @objc override func updateTheme() {
        super.updateTheme()
        
        guard let manager = ThemeManager.shared else {
            return
        }
        
        manager.update(navigationController)
        manager.updateBackground(of: view)
        
        dividerImageView.image = manager.themedImage(UIImage(named: "drag_icon.png"))
        view.backgroundColor = navigationController?.navigationBar.barTintColor
        navigationController?.navigationBar.barStyle = manager.isDarkTheme ? .black : .default
        
        tidyNavigationController()
    }
    
    /// Moves the story pages controller to a Grid layout cell content (automatically removing it from the previous parent).
    @objc func moveStoriesToGridCell(_ cellContent: UIView) {
        guard let storyPagesViewController else {
            return
        }
        
        print("🎈 moveStoriesToGridCell: \(storyPagesViewController.currentPage.activeStory["story_title"] ?? "none")")
        
        add(viewController: storyPagesViewController, to: cellContent, of: appDelegate.feedDetailViewController)
        
        adjustForAutoscroll()
    }
    
    /// Moves the story pages controller to the detail controller (automatically removing it from the previous parent).
    @objc func moveStoriesToDetail() {
        guard let storyPagesViewController else {
            return
        }
        
        let isTop = layout == .top
        let appropriateSuperview = isTop ? bottomContainerView : topContainerView
        
        if storyPagesViewController.view.superview != appropriateSuperview {
            add(viewController: storyPagesViewController, top: !isTop)
            
            adjustForAutoscroll()
        }
    }
    
    /// Adjusts the container when autoscrolling. Only applies to iPhone.
    @objc func adjustForAutoscroll() {
        adjustTopConstraint()
        updateTheme()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        updateLayout(reload: false)
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        
        adjustTopConstraint()
    }
    
    override func viewWillTransition(to size: CGSize, with coordinator: UIViewControllerTransitionCoordinator) {
        super.viewWillTransition(to: size, with: coordinator)
        
        if [.top, .bottom].contains(layout) {
            coordinator.animate { context in
                self.dividerViewBottomConstraint.constant = self.dividerPosition
            }
        }
        
        adjustTopConstraint()
    }
    
    private func adjustTopConstraint() {
        if UIDevice.current.userInterfaceIdiom != .phone {
            if view.window?.windowScene?.traitCollection.horizontalSizeClass == .compact {
                topContainerTopConstraint.constant = -50
            } else {
                topContainerTopConstraint.constant = 0
            }
        } else if let controller = storyPagesViewController, !controller.isNavigationBarHidden {
            topContainerTopConstraint.constant = -44
        } else {
            topContainerTopConstraint.constant = 0
        }
    }
    
    private var isDraggingDivider = false
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first
        
        guard let point = touch?.location(in: view) else {
            return
        }
        
        let isInside = dividerView.frame.contains(point)
        
        guard touch?.view == dividerView || isInside || isDraggingDivider else {
            return
        }
        
        isDraggingDivider = true
        
        let position = view.frame.height - point.y - 6
        
        guard position > 150, position < view.frame.height - 200 else {
            return
        }
        
        dividerPosition = position
        dividerViewBottomConstraint.constant = position
        view.setNeedsLayout()
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        isDraggingDivider = false
    }
}

private extension DetailViewController {
    func checkViewControllers() {
        let isTop = layout == .top
        
        if layout == .left {
            if feedDetailViewController != nil {
                remove(viewController: feedDetailViewController)
                
                feedDetailViewController = nil
                supplementaryFeedDetailViewController?.storiesCollection = appDelegate.storiesCollection
                appDelegate.feedDetailNavigationController = supplementaryFeedDetailNavigationController
                appDelegate.feedDetailViewController = supplementaryFeedDetailViewController
                appDelegate.splitViewController.setViewController(supplementaryFeedDetailNavigationController, for: .supplementary)
                supplementaryFeedDetailNavigationController = nil
                supplementaryFeedDetailViewController = nil
            }
            
            dividerViewBottomConstraint.constant = -13
            wasGrid = false
        } else if layout == .grid {
            if feedDetailViewController == nil || !wasGrid {
                remove(viewController: feedDetailViewController)
                
                feedDetailViewController = Storyboards.shared.controller(withIdentifier: .feedDetail) as? FeedDetailViewController
                feedDetailViewController?.storiesCollection = appDelegate.storiesCollection
                
                add(viewController: feedDetailViewController, top: true)
                
                if appDelegate.feedDetailNavigationController != nil {
                    supplementaryFeedDetailNavigationController = appDelegate.feedDetailNavigationController
                }
                
                supplementaryFeedDetailViewController = appDelegate.feedDetailViewController
                appDelegate.feedDetailNavigationController = nil
                appDelegate.feedDetailViewController = feedDetailViewController
                appDelegate.splitViewController.setViewController(nil, for: .supplementary)
            } else {
                add(viewController: feedDetailViewController, top: true)
            }
            
            dividerViewBottomConstraint.constant = -13
            wasGrid = true
        } else {
            if feedDetailViewController == nil || wasGrid {
                remove(viewController: feedDetailViewController)
                
                feedDetailViewController = Storyboards.shared.controller(withIdentifier: .feedDetail) as? FeedDetailViewController
                feedDetailViewController?.storiesCollection = appDelegate.storiesCollection
                
                add(viewController: feedDetailViewController, top: isTop)
                
                if appDelegate.feedDetailNavigationController != nil {
                    supplementaryFeedDetailNavigationController = appDelegate.feedDetailNavigationController
                }
                
                supplementaryFeedDetailViewController = appDelegate.feedDetailViewController
                appDelegate.feedDetailNavigationController = nil
                appDelegate.feedDetailViewController = feedDetailViewController
                appDelegate.splitViewController.setViewController(nil, for: .supplementary)
            } else {
                let appropriateSuperview = isTop ? topContainerView : bottomContainerView
                
                if feedDetailViewController?.view.superview != appropriateSuperview {
                    add(viewController: feedDetailViewController, top: isTop)
                }
            }
            
            dividerViewBottomConstraint.constant = dividerPosition
            
            appDelegate.updateSplitBehavior()
            wasGrid = false
        }
        
        appDelegate.feedDetailViewController.changedLayout()
        
        if layout != .grid {
            moveStoriesToDetail()
        }
    }
    
    func add(viewController: UIViewController?, top: Bool) {
        if top {
            add(viewController: viewController, to: topContainerView)
        } else {
            add(viewController: viewController, to: bottomContainerView)
        }
    }
    
    func add(viewController: UIViewController?, to containerView: UIView, of containerController: UIViewController? = nil) {
        guard let viewController else {
            return
        }
        
        let containerController = containerController ?? self
        
        containerController.addChild(viewController)
        
        containerView.addSubview(viewController.view)
        
        viewController.view.translatesAutoresizingMaskIntoConstraints = false
        viewController.view.leadingAnchor.constraint(equalTo: containerView.leadingAnchor).isActive = true
        viewController.view.trailingAnchor.constraint(equalTo: containerView.trailingAnchor).isActive = true
        viewController.view.topAnchor.constraint(equalTo: containerView.topAnchor).isActive = true
        viewController.view.bottomAnchor.constraint(equalTo: containerView.bottomAnchor).isActive = true
        
        viewController.didMove(toParent: containerController)
    }
    
    func remove(viewController: UIViewController?) {
        guard let viewController else {
            return
        }
        
        viewController.willMove(toParent: nil)
        viewController.removeFromParent()
        viewController.view.removeFromSuperview()
    }
    
    /// The status bar portion of the navigation controller isn't the right color, due to a white subview bleeding through the visual effect view. This somewhat hacky function will correct that.
    func tidyNavigationController() {
        guard let visualEffectSubviews = navigationController?.navigationBar.subviews.first?.subviews.first?.subviews, visualEffectSubviews.count == 3, visualEffectSubviews[1].alpha == 1 else {
            return
        }
        
        navigationController?.navigationBar.subviews.first?.backgroundColor = UINavigationBar.appearance().backgroundColor
    }
}
